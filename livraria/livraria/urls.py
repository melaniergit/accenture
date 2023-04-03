from django.contrib import admin
from django.urls import include, path, include
from rest_framework import routers
from livros.api import viewsets as livrosviewsets

route = routers.DefaultRouter()
route.register(r'livros',livrosviewsets.LivrosViewSet, basename="Livros")




urlpatterns = [
     path('admin/', admin.site.urls),
    path('', include(route.urls))
]
