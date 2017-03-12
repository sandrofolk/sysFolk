from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


# class User(AbstractUser):
#     pass


class Person(models.Model):
    name = models.CharField(_('name'), max_length=255)
    is_customer = models.BooleanField(_('is customer'), default=False)
    is_supplier = models.BooleanField(_('is supplier'), default=False)

    def __str__(self):
        return self.name

    @staticmethod
    def autocomplete_search_fields():
        return 'name',

    class Meta:
        verbose_name = _('person')
        verbose_name_plural = _('persons')
