from django.contrib import admin
from contact.models import *


# Register your models here.


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email', 'phone_extension', 'phone', 'subject', 'message',)
    list_filter = ()
    search_fields = (
        'user__email',
        'user__first_name',
        'user__last_name',
        'first_name',
        'last_name',
        'email',
        'phone',
        'subject',
        'message',
    )
    list_editable = ()
    autocomplete_fields = ('user',)
