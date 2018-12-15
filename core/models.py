from django.db import models

class Planeta(models.Model):
    nome = models.CharField(max_length=80, null=True, blank=True)
    clima = models.CharField(max_length=80, null=True, blank=True)
    terreno = models.CharField(max_length=80, null=True, blank=True)
    qtde_planetas = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nome