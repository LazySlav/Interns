from unittest import skip
from django.test import TestCase
import ast

class APICompanyTest(TestCase):
    def post_helper(self, test_data = None):
        if not test_data:
            test_data={"name":"test_name","legal_address":"abb","physical_address":"abbb","phone":"+79205267168","mail":"test@mail.ru"}
        return self.client.post("/companies/", test_data)
    def test_post(self):
        response = self.post_helper()
        self.assertEqual(response.status_code, 201)
    @skip
    def test_get(self):
        post_response = self.post_helper()
        content = ast.literal_eval(post_response.content.decode('utf-8'))
        test_id = content["id"]
        get_response = self.client.get(f"/companies/{test_id}",{"id":test_id})
        self.assertEqual(get_response.status_code,200)
    @skip
    def test_put(self):
        post_response = self.post_helper()
        content = ast.literal_eval(post_response.content.decode('utf-8'))
        test_id = content["id"]
        new_data = {"name":"new_test_name"}
        put_response = self.client.post(f"/companies/{test_id}",new_data)
        self.assertEqual(put_response.status_code,200)
    @skip
    def test_delete(self):
        post_response = self.post_helper()
        content = ast.literal_eval(post_response.content.decode('utf-8'))
        test_id = content["id"]
        delete_response = self.client.delete(f"/companies/{test_id}",{"id":test_id})
        # ? same as with test_get()
        self.assertEqual(delete_response.status_code, 200)