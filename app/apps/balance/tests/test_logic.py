from django.test import TestCase
from django.urls import reverse

from apps.account.models import Account
from apps.balance.models import Bill


class AccountTransactionTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # create users
        cls.admin = Account.objects.create(username='admin', first_name='Big', last_name='Bob')
        cls.user1 = Account.objects.create(username='user1', first_name='Big', last_name='Jon')
        cls.user2 = Account.objects.create(username='user2', first_name='Big', last_name='Andy')

        # create bills
        # cls.admin_bill_1 = Bill.objects.create()
        # cls.admin_bill_2 = Bill.objects.create()
        # cls.admin_bill_3 = Bill.objects.create()
        #
        # cls.user1_bill_1 = Bill.objects.create()
        # cls.user1_bill_2 = Bill.objects.create()
        #
        # cls.user2_bill_1 = Bill.objects.create()

    def test_ok(self):
        """Test ok"""
        print("ok")
