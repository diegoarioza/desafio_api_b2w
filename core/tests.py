from rest_framework.test import APIClient, APITestCase



class StartWarsTest(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get_empty(self):
        resp = self.client.get('/starwars/')

        self.assertEquals(resp.status_code, 200)


    def test_create_Dagobah(self):
        # this post should return 'qtde_planetas == 3 and nome == Dagobah
        resp = self.client.post('/starwars/', data={'nome': 'Dagobah'})
        self.assertEquals('Dagobah', resp.data.get('nome'))
        self.assertEquals(3, resp.data.get('qtde_planetas'))
        print(resp.data)

    def test_get_all(self):
        resp = self.client.get('/starwars/')
        print(resp.data)

