from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    company = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    job = models.CharField(max_length=200, null=True, blank=True)

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.username
