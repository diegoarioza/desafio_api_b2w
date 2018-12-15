from django.db import models

class Planeta(models.Model):
    nome = models.CharField(max_length=80)
    clima = models.CharField(max_length=80)
    terreno = models.CharField(max_length=80)

    def __str__(self):
        return self.nome