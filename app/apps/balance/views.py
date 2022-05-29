from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.views.generic import CreateView

from .forms import TransactionForm
from .models import AccountBillTransaction, Bill, BillTransaction


class AccountTransactionCreateView(LoginRequiredMixin, CreateView):
    model = AccountBillTransaction
    form_class = TransactionForm
    template_name = 'balance/transaction_create.html'

    def get_object(self):
        return self.request.user

    def get_form_kwargs(self):
        """Прокидываем юзера в форму"""
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        """Фильтруем и добавляем данные в контекст"""
        context = super(AccountTransactionCreateView, self).get_context_data()

        user = self.get_object()
        bills = Bill.objects.filter(user=user)
        context['bills'] = bills.values()  # список счетов
        context['balance'] = bills.aggregate(Sum('balance')).get("balance__sum")  # общая сумма
        # context['account_transactions'] = AccountBillTransaction.objects.filter(from_bills__user=user).order_by('-created_at').distinct()
        # context['bill_transactions'] = BillTransaction.objects.filter(from_bill__user=user).order_by('-created_at')

        context['account_transactions'] = AccountBillTransaction.objects.prefetch_related('from_bills__user').order_by(
            '-created_at')
        context['bill_transactions'] = BillTransaction.objects.select_related('from_bill__user').order_by('-created_at')
        return context
