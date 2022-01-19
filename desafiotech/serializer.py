from dataclasses import Field
from pyexpat import model
from rest_framework import serializers
from desafiotech.models import Region
from desafiotech.models import Fruit

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = '__all__'