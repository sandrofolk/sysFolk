from django.contrib import admin
from django.contrib.admin import register
# from jet.filters import RelatedFieldAjaxListFilter

from sysfolk.financial.models import AccountReceivable, AccountPayable, Category, DepositAccount, Bank, \
    ClassificationCenter


@register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    search_fields = ('description',)
    list_display = ('description',)


@register(Bank)
class BankModelAdmin(admin.ModelAdmin):
    search_fields = ('description',)
    list_display = ('description',)


@register(DepositAccount)
class DepositAccountModelAdmin(admin.ModelAdmin):
    search_fields = ('description',)
    list_display = ('description',)


@register(ClassificationCenter)
class ClassificationCenterModelAdmin(admin.ModelAdmin):
    search_fields = ('description',)
    list_display = ('description',)


@register(AccountReceivable)
class AccountReceivableModelAdmin(admin.ModelAdmin):
    list_filter = ('customer',)
    # list_filter = (
    #     ('customer', RelatedFieldAjaxListFilter),
    # )
    search_fields = ('description',)
    list_display = ('due_date', 'amount', 'description', 'customer', 'situation')


@register(AccountPayable)
class AccountPayableModelAdmin(admin.ModelAdmin):
    list_filter = ('supplier',)
    # list_filter = (
    #     ('provider', RelatedFieldAjaxListFilter),
    # )
    search_fields = ('description',)
    list_display = ('due_date', 'amount', 'description', 'supplier', 'situation')
