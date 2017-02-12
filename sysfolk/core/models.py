from django.db import models
from django.utils.translation import ugettext as _


class Person(models.Model):
    name = models.CharField(_('name'), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('person')
        verbose_name_plural = _('persons')
