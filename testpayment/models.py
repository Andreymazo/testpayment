from django.db import models

NULLABLE = {'blank': True, 'null': True}

class OurOrganization(models.Model):
    title = models.CharField(**NULLABLE)
    inn = models.PositiveIntegerField()
    balance = models.IntegerField()

    class Meta:
        verbose_name = "Наша организация"
        

    def __str__(self):
        """Строковое представление объекта Наша организация."""
        return f"{self.title}"

class CounterOrganization(models.Model):
    title = models.CharField(**NULLABLE)
    inn = models.PositiveIntegerField(unique=True)

    class Meta:
        verbose_name ="Контрагент"
        verbose_name_plural = "Контрагенты"

    def __str__(self):
        """Строковое представление объекта Контрагент."""
        return f"{self.title}"
    

"""Модель Платеж"""
class Payment(models.Model):
    ourorg = models.ForeignKey('testpayment.OurOrganization', related_name='payment1', on_delete=models.CASCADE)
    operation_id = models.CharField()
    amount = models.PositiveIntegerField()
    counterorg = models.ForeignKey('testpayment.CounterOrganization', related_name='payment2', on_delete=models.CASCADE)
    document_number = models.CharField()
    document_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"


    def __str__(self):
        """Строковое представление объекта Платеж."""
        return f"{self.id}"

"""Модель Банковский Платеж. Не связан ни с чем. Эта модель для эмуляции. И потому что в задании стоит Пост. чтото надо вносить кудато"""
class BankPayment(models.Model):
    operation_id = models.CharField(unique=True)
    amount = models.PositiveIntegerField()
    payer_inn = models.CharField()
    document_number = models.CharField()
    document_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Банковский Платеж"
        verbose_name_plural = "Банковские Платежи"


    def __str__(self):
        """Строковое представление объекта Банковского Платеж."""
        return f"{self.id}"