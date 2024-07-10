from django_filters import rest_framework as filters
from api.models import Transactions


class DateFilter(filters.FilterSet):
    amount = filters.RangeFilter()

    class Meta:
        model = Transactions
        fields = ['amount',]