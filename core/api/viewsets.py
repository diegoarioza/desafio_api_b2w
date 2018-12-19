from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.response import Response
from .serializers import PlanetaSerializer
from rest_framework import status
from core.models import Planeta
import requests


class PlanetasViewSet(ModelViewSet):
    filter_backends = (filters.SearchFilter,)
    search_fields = ('$id', '$nome')

    def get_queryset(self):
        queryset = Planeta.objects.all()
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)

        if id:
            queryset = queryset.filter(id=id)

        if nome:
            queryset = queryset.filter(nome=nome)

        return queryset

    # Override Create
    def create(self, request, *args, **kwargs):
        # exist_planet_in_api = False
        nome = request.POST.get('nome', None)
        clima = request.POST.get('clima', None)
        terreno = request.POST.get('terreno', None)

        try:
            req_api = requests.get('https://swapi.co/api/planets/?search=' + nome)
            qtde_planetas = len(req_api.json().get('results', None)[0].get('films', None))
            # if qtde_planetas > 0: exist_planet_in_api = True
        except IndexError:
            qtde_planetas = 0

        # print(exist_planet_in_api)
        serializer = self.get_serializer(data={'nome':nome, 'clima':clima, 'terreno': terreno, 'qtde_planetas': qtde_planetas})
        serializer.is_valid(raise_exception=True)

        if Planeta.objects.filter(nome=nome).exists():
            custom_msg = {'msg': 'Planeta ja esta cadastrado, por favor tente atualizar os dados do planeta.'}
            headers = self.get_success_headers(serializer.data)
            return Response(custom_msg, status=status.HTTP_201_CREATED, headers=headers)
        else:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    serializer_class = PlanetaSerializer