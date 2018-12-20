from rest_framework.test import APIClient, APITestCase
import json

class StartWarsTest(APITestCase):

    def setUp(self):
        self.user = 0

        self.client = APIClient()

    def teste1(self):
        resp = self.client.get('/starwars/')

        self.assertEquals(resp.status_code, 200)

    def teste2(self):
        resp = self.client.get('/starwars/6/')

        self.assertEquals(resp.status_code, 200)
