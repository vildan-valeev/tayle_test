import uuid

from django.db import models


class UUIDModel(models.Model):
    """Abstract model with `uuid` id as primary key."""

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False, null=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, editable=False, null=True, verbose_name='Обновлен')

    class Meta:
        abstract = True
