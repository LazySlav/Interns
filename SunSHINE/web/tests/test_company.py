import unittest
import requests
from test_data import COMPANY
URL = "http://127.0.0.1:8000/companies/"

class APICompanyTest(unittest.TestCase):
    def test_get(self):
        response = requests.get(URL, data=COMPANY[0])
        print(str(response.content))
    def test_post(self):
        response = requests.post(URL, data=COMPANY[1])
        print(str(response.content))
    def test_put(self):
        response = requests.post(URL, data=COMPANY[2])
        print(str(response.content))
    def test_delete(self):
        response = requests.post(URL, data=COMPANY[3])
        print(str(response.content))


if __name__ == '__main__':
    unittest.main()