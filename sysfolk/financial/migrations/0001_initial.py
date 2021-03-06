# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 11:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountPayable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('N', 'Normal'), ('P', 'Parcelled'), ('R', 'Recurrent')], default='N', max_length=1, verbose_name='type')),
                ('description', models.CharField(max_length=255, verbose_name='description')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='amount')),
                ('due_date', models.DateField(default=datetime.date.today, verbose_name='due_date')),
                ('document', models.CharField(blank=True, max_length=255, null=True, verbose_name='document')),
                ('emission_date', models.DateField(blank=True, null=True, verbose_name='emission_date')),
                ('observation', models.TextField(blank=True, null=True, verbose_name='observation')),
                ('situation', models.CharField(choices=[('U', 'Unpaid'), ('P', 'Paid'), ('C', 'Conciliated')], default='U', editable=False, max_length=1, verbose_name='situation')),
            ],
            options={
                'verbose_name_plural': 'accounts payable',
                'verbose_name': 'account payable',
            },
        ),
        migrations.CreateModel(
            name='AccountReceivable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('N', 'Normal'), ('P', 'Parcelled'), ('R', 'Recurrent')], default='N', max_length=1, verbose_name='type')),
                ('description', models.CharField(max_length=255, verbose_name='description')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='amount')),
                ('due_date', models.DateField(default=datetime.date.today, verbose_name='due_date')),
                ('document', models.CharField(blank=True, max_length=255, null=True, verbose_name='document')),
                ('emission_date', models.DateField(blank=True, null=True, verbose_name='emission_date')),
                ('observation', models.TextField(blank=True, null=True, verbose_name='observation')),
                ('situation', models.CharField(choices=[('U', 'Unpaid'), ('P', 'Paid'), ('C', 'Conciliated')], default='U', editable=False, max_length=1, verbose_name='situation')),
            ],
            options={
                'verbose_name_plural': 'accounts receivable',
                'verbose_name': 'account receivable',
            },
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255, verbose_name='description')),
            ],
            options={
                'verbose_name_plural': 'banks',
                'verbose_name': 'bank',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255, verbose_name='description')),
            ],
            options={
                'verbose_name_plural': 'categories',
                'verbose_name': 'category',
            },
        ),
        migrations.CreateModel(
            name='ClassificationCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255, verbose_name='description')),
            ],
            options={
                'verbose_name_plural': 'classification centers',
                'verbose_name': 'classification center',
            },
        ),
        migrations.CreateModel(
            name='DepositAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255, verbose_name='description')),
                ('agency_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='agency number')),
                ('agency_digit', models.CharField(blank=True, max_length=2, null=True, verbose_name='agency digit')),
                ('account_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='account number')),
                ('account_digit', models.CharField(blank=True, max_length=2, null=True, verbose_name='account digit')),
                ('bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='financial.Bank', verbose_name='bank')),
            ],
            options={
                'verbose_name_plural': 'deposit accounts',
                'verbose_name': 'deposit account',
            },
        ),
        migrations.AddField(
            model_name='accountreceivable',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='financial.Category', verbose_name='category'),
        ),
        migrations.AddField(
            model_name='accountreceivable',
            name='classification_center',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='financial.ClassificationCenter', verbose_name='classification center'),
        ),
        migrations.AddField(
            model_name='accountreceivable',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Person', verbose_name='customer'),
        ),
        migrations.AddField(
            model_name='accountreceivable',
            name='expected_deposit_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='financial.DepositAccount', verbose_name='expected deposit account'),
        ),
        migrations.AddField(
            model_name='accountpayable',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='financial.Category', verbose_name='category'),
        ),
        migrations.AddField(
            model_name='accountpayable',
            name='classification_center',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='financial.ClassificationCenter', verbose_name='classification center'),
        ),
        migrations.AddField(
            model_name='accountpayable',
            name='expected_deposit_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='financial.DepositAccount', verbose_name='expected deposit account'),
        ),
        migrations.AddField(
            model_name='accountpayable',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Person', verbose_name='supplier'),
        ),
    ]
