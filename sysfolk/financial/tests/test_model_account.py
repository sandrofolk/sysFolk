import datetime
from django.test import TestCase

from sysfolk.core.models import Person
from sysfolk.financial.admin import admin, AccountReceivableModelAdmin, AccountPayableModelAdmin
from sysfolk.financial.models import AccountReceivable, AccountPayable


def get_fields_can_be_blank():
    contents = [
        'category',
        'document',
        'emission_date',
        'expected_deposit_account',
        'classification_center',
        'observation',
    ]
    return contents


class AccountReceivableModelTest(TestCase):
    def setUp(self):
        self.description = 'Conta a Receber Teste'
        self.accountReceivable = AccountReceivable.objects.create(
            type=AccountReceivable.NORMAL,
            description=self.description,
            amount=1234.56,
            due_date=datetime.date.today(),
            situation=AccountReceivable.UNPAID,
        )

    def test_str(self):
        self.assertEqual(self.description, str(self.accountReceivable))

    def test_fields_can_be_blank(self):
        contents = get_fields_can_be_blank()
        contents += ['customer',]

        for expected in contents:
            with self.subTest():
                field = AccountReceivable._meta.get_field(expected)
                self.assertTrue(field.blank)

    def test_situation_not_editable(self):
        field = AccountReceivable._meta.get_field('situation')
        self.assertFalse(field.editable)


class AccountReceivableAdminTest(TestCase):
    def setUp(self):
        self.model_admin = AccountReceivableModelAdmin(AccountReceivable, admin.site)

    def test_search_fields(self):
        self.assertNotEqual(self.model_admin.search_fields, ())

    def test_list_display(self):
        self.assertNotEqual(self.model_admin.list_display, ('__str__',))


class AccountPayableModelTest(TestCase):
    def setUp(self):
        self.description = 'Conta a Pagar Teste'
        self.accountPayable = AccountPayable.objects.create(
            type=AccountPayable.NORMAL,
            description=self.description,
            amount=1234.56,
            due_date=datetime.date.today(),
            situation=AccountReceivable.UNPAID,
        )

    def test_str(self):
        self.assertEqual(self.description, str(self.accountPayable))

    def test_fields_can_be_blank(self):
        contents = get_fields_can_be_blank()
        contents += ['supplier',]

        for expected in contents:
            with self.subTest():
                field = AccountPayable._meta.get_field(expected)
                self.assertTrue(field.blank)

    def test_situation_not_editable(self):
        field = AccountPayable._meta.get_field('situation')
        self.assertFalse(field.editable)


class AccountPayableAdminTest(TestCase):
    def setUp(self):
        self.model_admin = AccountPayableModelAdmin(AccountPayable, admin.site)

    def test_search_fields(self):
        self.assertNotEqual(self.model_admin.search_fields, ())

    def test_list_display(self):
        self.assertNotEqual(self.model_admin.list_display, ('__str__',))
