from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from .models import Account

# Create your views here.
class AccountDetail(LoginRequiredMixin, DetailView):
    model = Account
    context_object_name = "account"
    template_name = 'account/account_detail.html'

    def get_object(self):
        return self.request.user
