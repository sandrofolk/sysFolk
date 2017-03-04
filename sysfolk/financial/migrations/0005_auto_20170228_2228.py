# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 22:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0004_auto_20170228_2200'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BankAccount',
            new_name='Bank',
        ),
        migrations.AlterModelOptions(
            name='bank',
            options={'verbose_name': 'bank', 'verbose_name_plural': 'banks'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='classificationcenter',
            options={'verbose_name': 'classification center', 'verbose_name_plural': 'classification centers'},
        ),
        migrations.AlterModelOptions(
            name='depositaccount',
            options={'verbose_name': 'deposit account', 'verbose_name_plural': 'deposit accounts'},
        ),
        migrations.RemoveField(
            model_name='depositaccount',
            name='bank_account',
        ),
        migrations.AddField(
            model_name='depositaccount',
            name='bank',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='financial.Bank', verbose_name='bank'),
        ),
    ]
