from django.test import TestCase
from sysfolk.financial.admin import admin, BankModelAdmin
from sysfolk.financial.models import Bank


class BankModelTest(TestCase):
    def setUp(self):
        self.description = 'Bank 1'
        self.bank = Bank.objects.create(
            description=self.description,
        )

    def test_str(self):
        self.assertEqual(self.description, str(self.bank))


class BankAdminTest(TestCase):
    def setUp(self):
        self.model_admin = BankModelAdmin(Bank, admin.site)

    def test_search_fields(self):
        self.assertNotEqual(self.model_admin.search_fields, ())

    def test_list_display(self):
        self.assertNotEqual(self.model_admin.list_display, ('__str__',))
