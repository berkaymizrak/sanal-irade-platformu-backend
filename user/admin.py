from django.contrib import admin
from user.models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_superuser')

    ordering = ('id', )

    fieldsets = (
        (None, {'fields': ('password',)}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': (
            'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'
        )}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

#     def get_model_perms(self, request):
#         return {}
#
#     def has_change_permission(self, request, obj=None):
#         return obj and request.user.id == obj.id
