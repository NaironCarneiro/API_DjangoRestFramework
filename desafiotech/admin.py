from csv import list_dialects
from re import search
from django.contrib import admin
from desafiotech.models import Region
from desafiotech.models import Fruit

class Regions(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

class Fruits(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields =('name',)

admin.site.register(Region,Regions)
admin.site.register(Fruit,Fruits)