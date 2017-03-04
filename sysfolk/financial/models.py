from django.db import models
import datetime
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    description = models.CharField(_('description'), max_length=255)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class Bank(models.Model):
    description = models.CharField(_('description'), max_length=255)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = _('bank')
        verbose_name_plural = _('banks')


class DepositAccount(models.Model):
    description = models.CharField(_('description'), max_length=255)
    bank = models.ForeignKey('Bank', verbose_name=_('bank'), on_delete=models.PROTECT, null=True,
                                     blank=True)
    agency_number = models.CharField(_('agency number'), max_length=20, null=True, blank=True)
    agency_digit = models.CharField(_('agency digit'), max_length=2, null=True, blank=True)
    account_number = models.CharField(_('account number'), max_length=20, null=True, blank=True)
    account_digit = models.CharField(_('account digit'), max_length=2, null=True, blank=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = _('deposit account')
        verbose_name_plural = _('deposit accounts')


class ClassificationCenter(models.Model):
    description = models.CharField(_('description'), max_length=255)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = _('classification center')
        verbose_name_plural = _('classification centers')


class Account(models.Model):
    NORMAL = 'N'
    PARCELLED = 'P'
    RECURRENT = 'R'
    TYPE_CHOICES = (
        (NORMAL, _('Normal')),
        (PARCELLED, _('Parcelled')),
        (RECURRENT, _('Recurrent')),
    )
    type = models.CharField(_('type'), max_length=1, choices=TYPE_CHOICES, default=NORMAL)

    description = models.CharField(_('description'), max_length=255)
    amount = models.DecimalField(_('amount'), max_digits=20, decimal_places=2)
    due_date = models.DateField(_('due_date'), default=datetime.date.today)
    category = models.ForeignKey('Category', verbose_name=_('category'), on_delete=models.PROTECT, null=True,
                                 blank=True)
    document = models.CharField(_('document'), max_length=255, null=True, blank=True)
    emission_date = models.DateField(_('emission_date'), null=True, blank=True)
    expected_deposit_account = models.ForeignKey('DepositAccount', verbose_name=_('expected deposit account'),
                                                 on_delete=models.PROTECT, null=True, blank=True)
    classification_center = models.ForeignKey('ClassificationCenter', verbose_name=_('classification center'),
                                              on_delete=models.PROTECT, null=True, blank=True)
    observation = models.TextField(_('observation'), null=True, blank=True)

    UNPAID = 'U'
    PAID = 'P'
    CONCILIATED = 'C'
    SITUATION_CHOICES = (
        (UNPAID, _('Unpaid')),
        (PAID, _('Paid')),
        (CONCILIATED, _('Conciliated')),
    )
    situation = models.CharField(_('situation'), max_length=1, choices=SITUATION_CHOICES, default=UNPAID,
                                 editable=False)

    def __str__(self):
        return self.description

    class Meta:
        abstract = True


class AccountReceivable(Account):
    customer = models.ForeignKey('core.Person', limit_choices_to={'is_customer': True}, verbose_name=_('customer'),
                                 on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = _('account receivable')
        verbose_name_plural = _('accounts receivable')


class AccountPayable(Account):
    supplier = models.ForeignKey('core.Person', limit_choices_to={'is_supplier': True}, verbose_name=_('supplier'),
                                 on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = _('account payable')
        verbose_name_plural = _('accounts payable')
