from django.db.models import Min

from apps.balance.models import AccountBillTransaction, BillTransaction


def transaction_many_to_one(instance: AccountBillTransaction):
    """Бизнес-логика транзакции при выборе нескольких счетов"""
    bills = instance.from_bills.all()
    # минимальный счет определяем, для равномерного снятия
    min_bill = bills.aggregate(Min('balance'))
    # минимально равные доли которые можно снимать
    min_need = instance.amount / len(bills)
    print(min_need, min_bill.get("balance__min"))
    # если остаток на самом минимальном счете превышает min_need(сумма разделенная на количество счетов),
    # то значит средств на всех счетах достаточно для снятия суммы. Пример в t_transaction.py
    if min_bill.get("balance__min") >= min_need:
        for bill in bills:
            BillTransaction.objects.create(
                from_bill=bill,
                to_bill=instance.to_bill,
                comment=instance.comment,
                reason=instance.reason,
                amount=min_need,
            )
        return True, 'Bills created'
    return False, "Bills create error (Недостаточно средств)"
