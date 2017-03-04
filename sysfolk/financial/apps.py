from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class FinancialConfig(AppConfig):
    name = 'sysfolk.financial'
    verbose_name = _('financial')
