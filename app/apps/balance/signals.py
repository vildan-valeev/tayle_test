from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from apps.balance.models import AccountBillTransaction


@receiver(m2m_changed, sender=AccountBillTransaction)
def save_price(sender, instance,  **kwargs):
    print(instance)
