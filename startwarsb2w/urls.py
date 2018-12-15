from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.api.viewsets import PlanetasViewSet
from core.models import Planeta

router = routers.DefaultRouter()
router.register(r'starwars', PlanetasViewSet, basename=Planeta)

urlpatterns = [
    path('', include(router.urls),),
    path('admin/', admin.site.urls)
]
