from django.test import TestCase
from web.models import CompanyModel


class CompanyModelTest(TestCase):
    def setUp(self):
        CompanyModel.objects.create(name="lion")
        CompanyModel.objects.create(name="cat")
    def direct_get(self):
        """Animals that can speak are correctly identified"""
        assert (lion:=CompanyModel.objects.get(name="lion")) is {"name":"lion"}
        assert (cat:=CompanyModel.objects.get(name="cat")) is {"name":"cat"}
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')