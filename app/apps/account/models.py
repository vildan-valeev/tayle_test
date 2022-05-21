from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    first_name = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="Имя"
    )
    last_name = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="Фамилия"
    )
    company = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="Компания"
    )
    phone = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name="Телефон"
    )
    country = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="Страна"
    )
    job = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="Работа"
    )

    def get_full_name(self):
        if self.first_name is None or self.last_name is None:
            return self.username
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.username
