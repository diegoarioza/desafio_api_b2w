from django.test import TestCase

from core.models import Planeta

class PlanetaTeste(TestCase):

    def setUp(self):
        self.planeta1 = Planeta.objects.create(nome='testeCase1')
        self.planeta1.save()


    def test1(self):
        self.assertEquals(self.planeta1,1)

