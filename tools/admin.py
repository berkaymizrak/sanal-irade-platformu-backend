from django.contrib import admin
from tools.models import *


# Register your models here.

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')
    list_editable = []

    class Meta:
        model = City


@admin.register(Town)
class TownAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    search_fields = ('name', 'city')
    list_editable = []

    class Meta:
        model = Town


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'postal_code', 'town')
    search_fields = ('name', 'postal_code', 'town')
    list_editable = []

    class Meta:
        model = District
