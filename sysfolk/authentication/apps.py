from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AuthenticationConfig(AppConfig):
    name = 'sysfolk.authentication'
    verbose_name = _('authentication')
