from django.test import TestCase
from sysfolk.financial.admin import admin, ClassificationCenterModelAdmin
from sysfolk.financial.models import ClassificationCenter


class ClassificationCenterModelTest(TestCase):
    def setUp(self):
        self.description = 'Classification Center 1'
        self.classificationCenter = ClassificationCenter.objects.create(
            description=self.description,
        )

    def test_str(self):
        self.assertEqual(self.description, str(self.classificationCenter))


class ClassificationCenterAdminTest(TestCase):
    def setUp(self):
        self.model_admin = ClassificationCenterModelAdmin(ClassificationCenter, admin.site)

    def test_search_fields(self):
        self.assertNotEqual(self.model_admin.search_fields, ())

    def test_list_display(self):
        self.assertNotEqual(self.model_admin.list_display, ('__str__',))
