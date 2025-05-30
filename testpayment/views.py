from rest_framework import generics

from django.urls import reverse
from rest_framework.decorators import api_view
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from testpayment.models import BankPayment, CounterOrganization, OurOrganization, Payment
from testpayment.serializers import BankPaymentCreationSerializer, CounterOrganizationSerializer, PaymentCreationSerializer
import requests
from django.shortcuts import get_object_or_404

"""Из задания ясно, что этот ендпоинт эмулирует апи создания Payment. Это не Пост,\
    а Гет. Мы здесь принимам джейсон и в зависимости от того, что приняли, либо создаем Платеж, либо нет. Сериализатор - лишнее"""
@csrf_exempt
@api_view(["POST"]) 
def payment_create(request, **kwargs):
    data_out = {
  "operation_id": "ccf0a86d-041b-4991-bcf7-e2352f7b8a4a",
  "amount": 145000,
  "payer_inn": "1234567890",
  "document_number": "PAY-328",
  "document_date": "2024-04-27T21:00:00Z"
}   
    data_new = { "ourorg":1, 
"operation_id": "ccf0a86d-041b-4991-bcf7-e2352f7b8a4a1",
  "amount": 145000,
  "counterorg": 1,
  "document_number": "PAY-328",
  "document_date": "2024-04-27T21:00:00Z"}
   
    # '-------------------------Если есть, то продолжаем ,если нет, то создаем КонтрАгента----------------------------------------------'
    
    if request.method == 'POST':
        serializer_item = BankPaymentCreationSerializer(data=request.data, context={'request': request})
        if serializer_item.is_valid():
            serializer_item.save()
            return Response(serializer_item.data, status=status.HTTP_201_CREATED)
        return Response(serializer_item.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({"message": "Got some data!", "data": request.data})

"""Запустим проект на какомнить другом порту и послушаем реквест с предыдущего ендпоинта"""
class BalanceInn(generics.RetrieveUpdateDestroyAPIView):
    queryset = CounterOrganization.objects.all()
    serializer_class = CounterOrganizationSerializer

 
    def get(self, request, **kwargs):
        inn=kwargs['inn']
        amount=kwargs['amount']
        item = CounterOrganization.objects.get(inn=inn)
        serializer = CounterOrganizationSerializer(item)
        ourorg_item = OurOrganization.objects.last()
        counterorg_item = CounterOrganization.objects.get(inn=request.data['inn'])
        payment_item = Payment.objects.create(
                ourorg = ourorg_item,
                operation_id=request.data['operation_id'],
                amount=request.data['amount'],
                counterorg = counterorg_item,
                document_number =request.data['document_number'],
                            )
        print('payment_item.pk', payment_item.pk)
        return Response(serializer.data)
