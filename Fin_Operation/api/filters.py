from django_filters import rest_framework as filters
from api.models import Transactions


class TransactionsFilter(filters.FilterSet):
    account = filters.AllValuesMultipleFilter(field_name="account")
    amount = filters.RangeFilter()
    date = filters.DateFromToRangeFilter()
    
    class Meta:
        model = Transactions
        fields = ['amount', 'date']