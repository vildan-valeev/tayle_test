from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, TemplateView

from .models import Account
from ..balance.models import Bill


class AccountDetail(LoginRequiredMixin, DetailView):
    model = Account
    context_object_name = "account"
    template_name = 'account/account_detail.html'

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(AccountDetail, self).get_context_data()
        bills = Bill.objects.filter(user=self.get_object())
        context['bills'] = bills.values()
        return context
