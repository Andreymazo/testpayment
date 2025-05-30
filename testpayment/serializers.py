from rest_framework import serializers
import requests
from testpayment.models import BankPayment, CounterOrganization, Payment

class CounterOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model=CounterOrganization
        fields = '__all__'


class PaymentCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields = '__all__'

class BankPaymentCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model=BankPayment
        fields = '__all__'

    def create(self, validated_data):
        print('validated_data', validated_data)

        if not str(validated_data['payer_inn']) in [str(i.inn) for i in CounterOrganization.objects.all()]:#Если нет такого КонтрАгента
                # , то сначала создаем Контрагента с новым инн
            counterorg_item = CounterOrganization.objects.create(inn=validated_data['payer_inn'])
            print('CounterOrg creqated ........................', 'id  ', counterorg_item.id, 'inn    ', counterorg_item.inn)
        counterorg_item = CounterOrganization.objects.get(inn=validated_data['payer_inn'])
            #------------------------ departure here----------------------
        inn = counterorg_item.inn
        amount = validated_data.get('amount')
            
        operation_id = validated_data.get('operation_id')
        document_number = validated_data.get('document_number')
        # bankpayment_data = validated_data
        bankpayment = BankPayment.objects.create(**validated_data)

        response = requests.get(f'http://0.0.0.0:8001/api/organizations/{inn}/{amount}/', data={'operation_id':operation_id,  'amount':amount,'inn':inn, \
                             'document_number': document_number, 'document_date':bankpayment.document_date})  
        # Profile.objects.create(user=user, **profile_data)
        return bankpayment
