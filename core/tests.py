from rest_framework.test import APIClient, APITestCase


class StartWarsTest(APITestCase):

    def setUp(self):
        self.client = APIClient()


    def test_get_empty(self):
        resp = self.client.get('/starwars/')
        self.assertEquals(resp.status_code, 200)


    def test_create_and_return_planet_Dagobah(self):
        # this post should return 'qtde_planetas == 3 and nome == Dagobah
        resp = self.client.post('/starwars/', data={'nome': 'Dagobah'})

        # test status code
        self.assertEquals(resp.status_code, 201)
        # test return post
        self.assertEquals('Dagobah', resp.data.get('nome'))
        self.assertEquals(3, resp.data.get('qtde_planetas'))
        # test get after post
        resp = self.client.get('/starwars/')
        self.assertEquals(resp.status_code, 200)
        # test status code
        resp2 = list(resp.data[0].values())
        # test id
        self.assertEquals(resp2[0], 1)
        # test Nome
        self.assertEquals(resp2[1], 'Dagobah')
        # test return qtde_planetas
        self.assertEquals(resp2[4], 3)






