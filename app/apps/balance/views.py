from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from .forms import TransactionForm
from .models import AccountBillTransaction


class AccountTransactionCreateView(LoginRequiredMixin, CreateView):
    model = AccountBillTransaction
    form_class = TransactionForm
    template_name = 'balance/transaction_create.html'
    # fields = ['from_bills', 'to_bill', 'comment', 'amount']
