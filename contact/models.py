from core.models import AbstractModel
from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Message(AbstractModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default=None,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('User'),
    )
    first_name = models.CharField(
        default=None,
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_('First Name'),
    )
    last_name = models.CharField(
        default=None,
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_('Last Name'),
    )
    email = models.EmailField(
        default=None,
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_('Email'),
    )
    phone_extension = models.CharField(
        default='+90',
        max_length=6,
        verbose_name=_('Phone extension'),
    )
    phone = models.CharField(
        default=None,
        null=True,
        blank=True,
        max_length=15,
        verbose_name=_('Phone'),
        validators=(RegexValidator(r'^\d{7,15}$'),),
    )
    subject = models.CharField(
        max_length=255,
        verbose_name=_('Subject'),
    )
    message = models.TextField(
        verbose_name=_('Message'),
    )

    class Meta:
        ordering = ('-created_date',)
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'Message {self.user.get_full_name()} ({self.user.email})' if self.user else f'Message {self.get_full_name()} ({self.email})'
