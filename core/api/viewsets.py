from rest_framework.viewsets import ModelViewSet
from .serializers import PlanetaSerializer
from core.models import Planeta


class PlanetasViewSet(ModelViewSet):

    queryset = Planeta.objects.all()
    serializer_class = PlanetaSerializer