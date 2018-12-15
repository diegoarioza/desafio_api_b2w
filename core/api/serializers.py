from rest_framework.serializers import ModelSerializer
from core.models import Planeta


class PlanetaSerializer(ModelSerializer):
    class Meta:
        model = Planeta
        fields = ('id', 'nome', 'clima', 'terreno', 'qtde_planetas')