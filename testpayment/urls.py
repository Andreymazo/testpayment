from django.urls import include, path

from testpayment.apps import TestpaymentConfig
from testpayment.views import BalanceInn, payment_create

app_name = TestpaymentConfig.name

urlpatterns = [
   path('webhook/bank/', payment_create, name='webhook_bank'),
   path('organizations/<int:inn>/<int:amount>/', BalanceInn.as_view(), name='balance_inn'),
]