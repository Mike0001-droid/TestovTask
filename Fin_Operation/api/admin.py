from django.contrib import admin
from api.models import BankAccount, Transactions

@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'balance')


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'date', 'amount')
