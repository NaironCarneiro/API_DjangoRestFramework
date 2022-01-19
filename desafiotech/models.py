from calendar import c
from operator import mod
from os import name
from unittest.util import _MAX_LENGTH
from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Fruit(models.Model):
    name = models.CharField(max_length=50)
    region = models.ForeignKey(Region,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name