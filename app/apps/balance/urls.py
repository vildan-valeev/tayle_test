from django.urls import path

from apps.balance.views import AccountTransactionCreateView

urlpatterns = [
    path('create/', AccountTransactionCreateView.as_view(), name='transaction-create'),
]
