from http.client import SERVICE_UNAVAILABLE
from unicodedata import name
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from desafiotech.admin import Regions
from .models import Region, Fruit
from .serializer import RegionSerializer, FruitSerializer
from rest_framework import status

class RegionsList(APIView):
    
    def get(self, request):
            regions = Region.objects.all()
            serializer = RegionSerializer(regions, many = True)
            return Response(serializer.data)

    def post(self, request):
        serializer = RegionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegionsDetail(APIView): 

    def get_object(self, pk):
        try:
            return Region.objects.get(pk=pk)
        except Region.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        regions = self.get_object(pk)
        serializer = RegionSerializer(regions)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        regions = self.get_object(pk)
        serializer = RegionSerializer(regions, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        regions = self.get_object(pk)
        regions.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class FruitsList(APIView):
    
    def get(self, request):
            fruits = Fruit.objects.all()
            serializer = FruitSerializer(fruits, many = True)
            return Response(serializer.data)

    def post(self, request):
        serializer = FruitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FruitsDetail(APIView): 

    def get_object(self, pk):
        try:
            return Fruit.objects.get(pk=pk)
        except Fruit.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        fruits = self.get_object(pk)
        serializer = FruitSerializer(fruits)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        fruits = self.get_object(pk)
        serializer = FruitSerializer(fruits, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        fruits = self.get_object(pk)
        fruits.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


