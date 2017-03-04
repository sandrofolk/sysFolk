from django.test import TestCase
from sysfolk.financial.admin import admin, CategoryModelAdmin
from sysfolk.financial.models import Category


class CategoryModelTest(TestCase):
    def setUp(self):
        self.description = 'Categoria'
        self.category = Category.objects.create(
            description=self.description,
        )

    def test_str(self):
        self.assertEqual(self.description, str(self.category))


class CategoryAdminTest(TestCase):
    def setUp(self):
        self.model_admin = CategoryModelAdmin(Category, admin.site)

    def test_search_fields(self):
        self.assertNotEqual(self.model_admin.search_fields, ())

    def test_list_display(self):
        self.assertNotEqual(self.model_admin.list_display, ('__str__',))
