# Generated by Django 4.0.4 on 2022-05-19 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balance', '0002_alter_accountbilltransaction_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountbilltransaction',
            name='from_bills',
            field=models.ManyToManyField(to='balance.bill'),
        ),
    ]
