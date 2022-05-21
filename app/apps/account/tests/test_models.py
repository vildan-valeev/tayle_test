from django.test import TestCase
from django.urls import reverse

from apps.account.models import Account
from apps.balance.models import Bill


class AccountModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # create user
        cls.test_user = Account.objects.create(username="test_username", first_name='Big', last_name="Bob")
        cls.test_user2 = Account.objects.create(username="test_username2", first_name='Big')

    def test_first_name_label(self):
        field_label = self.test_user._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'Имя')

    def test_last_name_label(self):
        user = Account.objects.get(id=1)
        field_label = user._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'Фамилия')

    def test_company_label(self):
        field_label = self.test_user._meta.get_field('company').verbose_name
        self.assertEquals(field_label, 'Компания')

    def test_phone_label(self):
        field_label = self.test_user._meta.get_field('phone').verbose_name
        self.assertEquals(field_label, 'Телефон')

    def test_country_label(self):
        field_label = self.test_user._meta.get_field('country').verbose_name
        self.assertEquals(field_label, 'Страна')

    def test_job_label(self):
        field_label = self.test_user._meta.get_field('job').verbose_name
        self.assertEquals(field_label, 'Работа')

    def test_first_name_max_length(self):
        max_length = self.test_user._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 200)

    def test_last_name_max_length(self):
        max_length = self.test_user._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 200)

    def test_company_max_length(self):
        max_length = self.test_user._meta.get_field('company').max_length
        self.assertEquals(max_length, 200)

    def test_phone_max_length(self):
        max_length = self.test_user._meta.get_field('phone').max_length
        self.assertEquals(max_length, 20)

    def test_country_max_length(self):
        max_length = self.test_user._meta.get_field('country').max_length
        self.assertEquals(max_length, 200)

    def test_job_max_length(self):
        max_length = self.test_user._meta.get_field('job').max_length
        self.assertEquals(max_length, 200)

    def test_get_str(self):
        self.assertEquals(str(self.test_user), 'test_username')

    def test_get_full_name_method_correct(self):
        # 'Big Bob'
        self.assertEquals(self.test_user.get_full_name(), "Big Bob")
        # last_name is None - > 'test_username2'
        self.assertEquals(self.test_user2.get_full_name(), "test_username2")
