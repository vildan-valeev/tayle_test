import decimal

from django.test import TestCase
from django.urls import reverse

from apps.account.models import Account
from apps.balance.models import Bill, AccountBillTransaction, REASON_PURCHASE


class AccountTransactionTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # create users
        cls.admin = Account.objects.create(username='admin', first_name='Big', last_name='Bob')
        cls.user1 = Account.objects.create(username='user1', first_name='Big', last_name='Jon')
        cls.user2 = Account.objects.create(username='user2', first_name='Big', last_name='Andy')

    def test_ok(self):
        """Недостаточно средств на одном из счетов для перевода если выбраны несколько"""
        #Добавляем счета и балансы
        admin_bill_1 = Bill.objects.create(user=self.admin, balance=100)
        admin_bill_2 = Bill.objects.create(user=self.admin, balance=100)
        admin_bill_3 = Bill.objects.create(user=self.admin, balance=100)

        user1_bill_2 = Bill.objects.create(user=self.user1, balance=0)
        # Создаем транзакцию
        tr = AccountBillTransaction.objects.create(
            # from_bills=,
            to_bill=user1_bill_2,
            amount=300,
            comment="300",
            reason=REASON_PURCHASE)
        tr.from_bills.add(admin_bill_1, admin_bill_2, admin_bill_3)
        # Проверяем баланс кому был сделан перевод
        result = Bill.objects.get(id=user1_bill_2.id).balance
        self.assertEqual(result, decimal.Decimal(300), "Пример 1")
