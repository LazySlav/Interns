from unittest import skip, skipIf
from uuid import UUID
from django.test import TestCase
from web.models import CompanyModel


class APICompanyTest(TestCase):
    def test_post(self):
        test_data={"name":"test_name"}
        response = self.client.post("/companies/", test_data)
        self.assertEqual(response.status_code, 201)
    @skip("no entries in DB yet")
    def test_get(self):
        test_id = UUID()
        response = self.client.get(f"/companies/{test_id}")
        self.assertEqual(response.status_code,200)
