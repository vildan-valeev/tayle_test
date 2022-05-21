from django.test import TestCase

from apps.account.models import Account
from apps.balance.models import Bill


class BillModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.admin = Account.objects.create(username='admin', first_name='Big', last_name='Bob')
        cls.test_bill = Bill.objects.create(user=cls.admin, balance=500)

    def test_user_related_name(self):
        field_related_name = self.test_bill._meta.get_field('user').related_query_name()
        self.assertEquals(field_related_name, 'checking_accounts')
