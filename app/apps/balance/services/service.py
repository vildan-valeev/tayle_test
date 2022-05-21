from django.db.models import Min

from apps.balance.models import AccountBillTransaction, BillTransaction, REASON_CANCELED, REASON_PURCHASE

"""
Не используется явно принцип "жирные модели" и "жирные вьюхи". 
Все что самописное, бизнес-логика и тд - все в отдельные функции, классы, слои.
Необходимо для удобства тестирования.
"""


class TransactionLogic:
    def __init__(self, instance: AccountBillTransaction):
        self.instance = instance
        self.bills = instance.from_bills.all()  # счета отправителя
        print(self.bills)
        self.min_bill = self.bills.aggregate(Min('balance'))  # минимальный счет определяем, для равномерного снятия
        self.min_need = self.instance.amount / len(self.bills)  # минимально равные доли которые можно снимать

    def can_do_transaction(self):
        """Проверка на возможность отправки"""
        if self.min_bill.get("balance__min") >= self.min_need:
            return True, ""
        return False, "Transactions create error (Недостаточно средств)"

    def do_transaction(self):
        """Отправка средств между счетами - One to one"""
        for bill in self.bills:
            BillTransaction.objects.create(
                from_bill=bill,
                to_bill=self.instance.to_bill,
                comment=self.instance.comment,
                reason=REASON_PURCHASE,  # TODO: продумать логику на случай если отвалится сохранение
                amount=self.min_need,
            )
        return True, 'Transactions completed'

    def cancel_transaction(self):
        """Ставим статус отмена транзакции в REASON_CANCELED модели, деньги не переводим"""
        self.instance.reason = REASON_CANCELED
        self.instance.save()

    def billed_transaction(self):
        """Ставим статус ПОЛОЖИТЕЛЬНЫЙ в REASON_CANCELED модели, деньг переведены"""
        self.instance.reason = REASON_PURCHASE
        self.instance.save()
