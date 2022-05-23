from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.views.generic import CreateView

from .forms import TransactionForm
from .models import AccountBillTransaction, Bill, BillTransaction


class AccountTransactionCreateView(LoginRequiredMixin, CreateView):
    model = AccountBillTransaction
    form_class = TransactionForm
    template_name = 'balance/transaction_create.html'
    # fields = ['from_bills', 'to_bill', 'comment', 'amount']


    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(AccountTransactionCreateView, self).get_context_data()

        bills = Bill.objects.filter(user=self.get_object())
        context['bills'] = bills.values()  # список счетов
        context['balance'] = bills.aggregate(Sum('balance')).get("balance__sum") # общая сумма
        context['account_transactions'] = AccountBillTransaction.objects.all()
        context['bill_transactions'] = BillTransaction.objects.all()
        return context
