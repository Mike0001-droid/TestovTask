from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import generics
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import AllowAny
from api.models import BankAccount, Transactions
from api.serializers import BankAccountSerializer, TransactionsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from api.filters import TransactionsFilter


class BankAccountViewSet(GenericViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    permission_classes = (AllowAny, )

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransactionsViewSet(GenericViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer
    permission_classes = (AllowAny, )
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TransactionsFilter

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        try:
            account = BankAccount.objects.get(pk=request.data.get('account'))
            account.balance += request.data.get('amount')
            account.save()
        except ObjectDoesNotExist:
            return Response({'detail': 'Объекта не существует', 'error': {'Счёт': 'Объекта не существует'}}, 
                              status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            transactions = Transactions.objects.get(pk=pk)
            transactions.delete()
            transactions.save()
            return Response(status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'detail': 'Объекта не существует', 'error': {'Счёт': 'Объекта не существует'}}, 
                              status=status.HTTP_404_NOT_FOUND)
        

