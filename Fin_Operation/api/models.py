from django.db import models


class BankAccount(models.Model):
    name = models.CharField('Название банковского счёта', max_length=255)
    balance = models.FloatField('Текущий баланс счёта', default=0)

    def __str__(self):
        return f"{self.name} - {self.balance}"
    
    class Meta:
        verbose_name = 'Счёт'
        verbose_name_plural = 'Счета'


class Transactions(models.Model):
    account = models.ForeignKey(BankAccount, verbose_name='Банковский счёт', on_delete=models.CASCADE, related_name="account")
    date = models.DateField('Дата операции')
    amount = models.FloatField('Сумма операции')

    def __str__(self):
        return f"{self.date} - {self.account}"
    
    class Meta:
        verbose_name = 'Операция'
        verbose_name_plural = 'Операции'


