import uuid

from django.db.models import Model, UUIDField


class UUIDModel(Model):
    """Abstract model with `uuid` id as primary key."""

    id = UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    class Meta:
        abstract = True
