from django.core.management import BaseCommand

from testpayment.models import CounterOrganization, OurOrganization, Payment  


class Command(BaseCommand):

    def handle(self, *args, **options):
        # ourorg_item , _= OurOrganization.objects.all().get_or_create( title = 'Berezka', inn = 1234567, balance = 0)
        # print(ourorg_item)
        counterorg_item , _ = CounterOrganization.objects.all().get_or_create(title = 'Nemo2', inn = 1234567890)
        print('payer_inn', counterorg_item.inn)
#         # payer_inn
#         data_out = {
#             'ourorg': ourorg_item,
#             "operation_id": "ccf0a86d-041b-4991-bcf7-e2352f7b8a4a",
#             "amount": 145000,
#             "payer_inn": counterorg_item.inn,
#             "document_number": "PAY-328",
#             "document_date": "2024-04-27T21:00:00Z"
# }
        
#         item = Payment.objects.create(ourorg=ourorg_item, operation_id= "ccf0a86d-041b-4991-bcf7-e2352f7b8a4a", \
#                       counterorg_id=counterorg_item.pk, amount=145000, document_number= "PAY-328", document_date= "2024-04-27T21:00:00Z")
#         item.save()
#         print(item)
     