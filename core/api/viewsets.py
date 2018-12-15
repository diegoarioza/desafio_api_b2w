from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import PlanetaSerializer
from rest_framework import status
from core.models import Planeta
import requests


class PlanetasViewSet(ModelViewSet):
    amount_films = 0

    def get_queryset(self):
        queryset = Planeta.objects.all()
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)

        if id or nome:
            queryset = queryset.filter(id=id) | queryset.filter(nome=nome)

        return queryset

    def create(self, request, *args, **kwargs):
        nome = request.POST.get('nome', None)
        clima = request.POST.get('clima', None)
        terreno = request.POST.get('terreno', None)

        try:
            req_api = requests.get('https://swapi.co/api/planets/?search=' + nome)
            qtde_planetas = len(req_api.json().get('results', None)[0].get('films', None))
        except IndexError:
            qtde_planetas = 0


        ###############################################################################
        serializer = self.get_serializer(data={'nome':nome, 'clima':clima, 'terreno': terreno, 'qtde_planetas': qtde_planetas})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)


        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)




    serializer_class = PlanetaSerializer