from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from apps.balance.models import AccountBillTransaction


@receiver(m2m_changed, sender=AccountBillTransaction.from_bills.through)
def save_price(sender,  **kwargs):
    print(kwargs)
    print(kwargs['action'])

#
# @receiver(post_save, sender=AccountBillTransaction)
# def save_e(sender, instance,  **kwargs):
#     print(instance)
