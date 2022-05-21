# Generated by Django 4.0.4 on 2022-05-21 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='company',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Компания'),
        ),
        migrations.AlterField(
            model_name='account',
            name='country',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='account',
            name='job',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Работа'),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Телефон'),
        ),
    ]