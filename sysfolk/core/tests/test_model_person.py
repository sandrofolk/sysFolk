from django.test import TestCase

from sysfolk.core.models import Person
from sysfolk.core.admin import admin, PersonModelAdmin


class PersonModelTest(TestCase):
    def setUp(self):
        self.name = 'Alessandro'
        self.person = Person.objects.create(
            name=self.name
        )

    def test_str(self):
        self.assertEqual(self.name, str(self.person))

    # TODO: Falta testar se está obrigando uma pessoa ser ou cliente ou fornecedor!


class PersonAdminTest(TestCase):
    def setUp(self):
        self.model_admin = PersonModelAdmin(Person, admin.site)

    def test_search_fields(self):
        self.assertNotEqual(self.model_admin.search_fields, ())

    def test_list_display(self):
        self.assertNotEqual(self.model_admin.list_display, ('__str__',))
