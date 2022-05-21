# from django.db.models.signals import m2m_changed
# from django.dispatch import receiver
#
# from apps.balance.models import AccountBillTransaction
# from apps.balance.services.service import TransactionLogic


# @receiver(m2m_changed, sender=AccountBillTransaction.from_bills.through)
# def save_price(sender, action, instance,  **kwargs):
#     pass
#     print("M2M signal", kwargs)
#
#     if action == "post_add":
#         trans_process = TransactionLogic(instance)
#         can_transaction, msg = trans_process.can_do_transaction()
#         if can_transaction:
#             print("M2M signal", )
#             return trans_process.do_transaction()
#         trans_process.cancel_transaction()
