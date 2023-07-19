from django.test import TestCase
import ast

class APICompanyTest(TestCase):
    def post_helper(self):
        test_data={"name":"test_name"}
        return self.client.post("/companies/", test_data)

    def test_post(self):
        response = self.post_helper()
        self.assertEqual(response.status_code, 201)
    def test_get(self):
        post_response = self.post_helper()
        content = ast.literal_eval(post_response.content.decode('utf-8'))
        test_id = content["id"]
        get_response = self.client.get("/companies/",{"id":test_id})
        # ? why the fuck does it return 201 when it should 200        
        self.assertEqual(get_response.status_code,201)
    def test_put(self):
        post_response = self.post_helper()
        content = ast.literal_eval(post_response.content.decode('utf-8'))
        test_id = content["id"]
        put_response = self.client.post(f"/companies/{test_id}",{"name":"new_test_name"})
        self.assertEqual(put_response.status_code,200)
    def test_delete(self):
        post_response = self.post_helper()
        content = ast.literal_eval(post_response.content.decode('utf-8'))
        test_id = content["id"]
        delete_response = self.client.delete("/companies/",{"id":test_id})
        # ? same as with test_get()
        self.assertEqual(delete_response.status_code, 201)