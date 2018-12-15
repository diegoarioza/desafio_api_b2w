from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.api.viewsets import PlanetasViewSet

router = routers.DefaultRouter()
router.register(r'starwars', PlanetasViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls)
]
