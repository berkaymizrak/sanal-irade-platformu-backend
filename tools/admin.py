from django.contrib import admin
from tools.models import *
from parler.admin import TranslatableAdmin


# Register your models here.

@admin.register(City)
class CityAdmin(TranslatableAdmin):
    list_display = ('name', 'language_column', 'code', 'updated_date', 'created_date',)
    search_fields = ('translations__name', 'code',)
    list_editable = ()


@admin.register(Town)
class TownAdmin(TranslatableAdmin):
    list_display = ('name', 'language_column', 'city', 'updated_date', 'created_date',)
    search_fields = ('translations__name', 'city',)
    list_editable = ()

    class Meta:
        model = Town


@admin.register(District)
class DistrictAdmin(TranslatableAdmin):
    list_display = ('name', 'language_column', 'postal_code', 'town', 'updated_date', 'created_date',)
    search_fields = ('translations__name', 'postal_code', 'town',)
    list_editable = ()

    class Meta:
        model = District


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'icon', 'url', 'updated_date', 'created_date',)
    search_fields = ('url',)
    list_editable = ('order', 'url', 'icon',)

    class Meta:
        model = SocialMedia
