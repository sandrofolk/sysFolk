from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from sysfolk.core.models import User, Person

admin.site.site_header = _('sysFolk / ConTTudOweb')
admin.site.site_title = _('sysFolk')
admin.site.index_title = _('Home')


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Person)
class PersonModelAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)
