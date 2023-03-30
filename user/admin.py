from django.contrib import admin
from user.models import *
from django.contrib.auth.admin import UserAdmin


@admin.register(UserAuthorizedArea)
class UserAuthorizedAreaAdmin(admin.ModelAdmin):
    list_display = ('user', 'approved',)
    list_filter = ('approved',)
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'district__translations__name',)
    list_editable = ('approved',)
    autocomplete_fields = ('user', 'district',)


class UserAuthorizedAreaInline(admin.TabularInline):
    model = UserAuthorizedArea
    can_delete = False
    min_num = 1
    autocomplete_fields = ('district',)


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_superuser',)
    ordering = ('id',)
    fieldsets = (
        (None, {'fields': ('password',)}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email',)}),
        ('Detailed info', {'fields': ('identity_number', 'birth_year', 'phone_extension', 'phone',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)}),
        ('Important dates', {'fields': ('last_login', 'date_joined',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2',)}
         ),
        ('Detailed info', {
            'classes': ('wide',),
            'fields': ('identity_number', 'birth_year', 'phone_extension', 'phone',)}
         ),
        ('Permissions', {
            'classes': ('wide',),
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)}
         ),
    )
    inlines = [UserAuthorizedAreaInline, ]


@admin.register(GDPRConsent)
class GDPRConsentAdmin(admin.ModelAdmin):
    list_display = ('user', 'agreement', 'ip_address', 'is_accepted', 'updated_date', 'created_date',)
    list_filter = ('is_accepted', 'agreement',)
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'ip_address',)
    list_editable = ()
    autocomplete_fields = ('user',)
