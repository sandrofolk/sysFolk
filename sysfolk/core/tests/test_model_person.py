from django.test import TestCase

from sysfolk.core.models import Person


class PersonModelTest(TestCase):
    def setUp(self):
        self.name = 'Alessandro'
        self.person = Person.objects.create(
            name=self.name
        )

    def test_str(self):
        self.assertEqual(self.name, str(self.person))
