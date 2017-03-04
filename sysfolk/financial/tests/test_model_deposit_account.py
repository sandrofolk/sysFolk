from django.test import TestCase
from sysfolk.financial.admin import admin, DepositAccountModelAdmin
from sysfolk.financial.models import DepositAccount


class DepositAccountModelTest(TestCase):
    def setUp(self):
        self.description = 'Conta Bancária'
        self.depositAccount = DepositAccount.objects.create(
            description=self.description,
        )

    def test_str(self):
        self.assertEqual(self.description, str(self.depositAccount))

    def test_fields_can_be_blank(self):
        contents = [
            'bank',
            'agency_number',
            'agency_digit',
            'account_number',
            'account_digit',
        ]
        for expected in contents:
            with self.subTest():
                field = DepositAccount._meta.get_field(expected)
                self.assertTrue(field.blank)


class DepositAccountAdminTest(TestCase):
    def setUp(self):
        self.model_admin = DepositAccountModelAdmin(DepositAccount, admin.site)

    def test_search_fields(self):
        self.assertNotEqual(self.model_admin.search_fields, ())

    def test_list_display(self):
        self.assertNotEqual(self.model_admin.list_display, ('__str__',))
