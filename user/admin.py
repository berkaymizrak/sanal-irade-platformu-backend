from django.contrib import admin
from user.models import *
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_superuser',)
    ordering = ('id',)
    fieldsets = (
        (None, {'fields': ('password',)}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Detailed info', {'fields': ('identity_number', 'birth_year', 'phone_extension', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )


@admin.register(GDPRConsent)
class GDPRConsentAdmin(admin.ModelAdmin):
    list_display = ('user', 'agreement', 'ip_address', 'is_accepted', 'updated_date', 'created_date',)
    list_filter = ('is_accepted', 'agreement',)
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'ip_address',)
    list_editable = ()
