from django.contrib import admin
from django.urls import path, include
from desafiotech.serializer import FruitSerializer
from rest_framework import routers

urlpatterns = [
    path('',include('desafiotech.urls')),
    path('admin/', admin.site.urls),
    path('', include('rest_framework.urls')),
]
