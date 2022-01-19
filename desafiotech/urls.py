from django.urls import path
from .views import RegionsDetail, RegionsList, FruitsDetail, FruitsList


urlpatterns = [
    path('regions/<int:pk>/',RegionsDetail.as_view(), name = 'regions'),
    path('regions/',RegionsList.as_view(), name = 'regions'),
    path('fruits/<int:pk>/',FruitsDetail.as_view(), name = 'fruits'),
    path('fruits/',FruitsList.as_view(), name = 'fruits')

]