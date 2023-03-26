from django.contrib import admin
from tools.models import *


# Register your models here.

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'updated_date', 'created_date')
    search_fields = ('name', 'code')
    list_editable = []

    class Meta:
        model = City


@admin.register(Town)
class TownAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'updated_date', 'created_date')
    search_fields = ('name', 'city')
    list_editable = []

    class Meta:
        model = Town


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'postal_code', 'town', 'updated_date', 'created_date')
    search_fields = ('name', 'postal_code', 'town')
    list_editable = []

    class Meta:
        model = District


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'name', 'url', 'icon', 'updated_date', 'created_date']
    search_fields = ['name', 'url']
    list_editable = ['order', 'name', 'url', 'icon']

    class Meta:
        model = SocialMedia
