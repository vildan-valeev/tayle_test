import datetime
import decimal

from django.db import models, transaction

from apps.account.models import Account


class Bill(models.Model):
    """Счета"""
    MIN_ACTION_AMOUNT = decimal.Decimal(0)
    MAX_ACTION_AMOUNT = decimal.Decimal(1000000000)

    user = models.ForeignKey(Account, models.PROTECT, related_name="checking_accounts")
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    modified_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    balance = models.DecimalField(max_digits=20, decimal_places=6, default=decimal.Decimal(0))

    class Meta:
        verbose_name = "Счет"
        verbose_name_plural = "Счета"

    def __str__(self):
        if self.user:
            return f"UserID: {self.user.pk} Username: {self.user.username}"
        return "Internal account"


REASON_DEPOSITED = 'DEPOSITED'
REASON_PURCHASE = 'BILLED'
REASON_DEPOSITED = 'CANCELED'
REASON_PURCHASE_REFUND = 'REFUNDED'
REASON_OTHER = 'OTHER'
REASON_CHOICES = (
    (REASON_DEPOSITED, 'Deposited'),
    (REASON_PURCHASE, 'Billed'),
    (REASON_PURCHASE_REFUND, 'Refunded'),
    (REASON_OTHER, 'Other'),
)


class AccountBillTransaction(models.Model):
    """Транзакция между пользователями - из нескольких счетов в одну"""

    from_bills = models.ManyToManyField(Bill, blank=False)
    to_bill = models.ForeignKey(Bill, models.PROTECT, related_name="to_bill")
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True)
    comment = models.TextField()
    reason = models.CharField(max_length=255, null=False, choices=REASON_CHOICES, default=REASON_DEPOSITED)
    amount = models.DecimalField(max_digits=20, decimal_places=6)

    def __str__(self):
        return f"Transaction: ID {self.id} to --> {self.to_bill.user.username}. " \
               f"Amount {self.amount}"

    class Meta:
        verbose_name = "Транзакцию между пользователем"
        verbose_name_plural = "Транзакции между пользователями"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):

        super(AccountBillTransaction, self).save(force_insert=False, force_update=False, using=None,
                                          update_fields=None)

class BillTransaction(models.Model):
    """Транзакция между счетами пользователя"""

    from_bill = models.ForeignKey(Bill, models.PROTECT, related_name="from_account")
    to_bill = models.ForeignKey(Bill, models.PROTECT, related_name="to_account")
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True)
    comment = models.TextField()
    reason = models.CharField(max_length=255, blank=True, null=True, choices=REASON_CHOICES)
    amount = models.DecimalField(max_digits=20, decimal_places=6)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.pk:
            with transaction.atomic():
                bill_from = Bill.objects.select_for_update().get(id=self.from_bill.id)
                bill_to = Bill.objects.select_for_update().get(id=self.to_bill.id)

                now = datetime.datetime.utcnow()
                super(BillTransaction, self).save(force_insert=False, force_update=False, using=None,
                                                  update_fields=None)

                bill_from.balance += -self.amount
                bill_from.modified_at = now
                bill_from.save()

                bill_to.balance += self.amount
                bill_to.modified_at = now
                bill_to.save()

                account_from_balance_after = bill_from.balance
                account_to_balance_after = bill_to.balance

                BillEntry.objects.create(transaction=self, bill=bill_from,
                                         amount=-self.amount, created_at=now,
                                         balance_after_transaction=account_from_balance_after)
                BillEntry.objects.create(transaction=self, bill=bill_to,
                                         amount=self.amount, created_at=now,
                                         balance_after_transaction=account_to_balance_after)
                return self

    def __str__(self):
        return f"Transaction: {self.from_bill} --> {self.to_bill}. Amount {self.amount}"

    class Meta:
        verbose_name = "Транзакцию между счетами"
        verbose_name_plural = "Транзакции между счетами"


class BillEntry(models.Model):
    bill = models.ForeignKey(Bill, models.PROTECT, )
    transaction = models.ForeignKey(BillTransaction, models.PROTECT, )
    created_at = models.DateTimeField()
    amount = models.DecimalField(max_digits=20, decimal_places=6)
    balance_after_transaction = models.DecimalField(max_digits=20, decimal_places=6)

    def __str__(self):
        return f"{self.transaction}"

    class Meta:
        verbose_name = "Checking account entry"
        verbose_name_plural = "Checking account entries"
