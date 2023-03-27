from core.models import AbstractModel
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.conf import settings
from django.contrib.auth import get_user_model
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
        constraints = [
            models.CheckConstraint(
                check=(
                    models.Q(user__isnull=False) &
                    models.Q(first_name__isnull=True) &
                    models.Q(last_name__isnull=True) &
                    models.Q(email__isnull=True) &
                    models.Q(phone__isnull=True)
                ) | (
                    models.Q(user__isnull=True) &
                    models.Q(first_name__isnull=False) &
                    models.Q(last_name__isnull=False) &
                    models.Q(email__isnull=False) &
                    models.Q(phone__isnull=False)
                ),
                name='only_one_of_user_or_email_first_name_last_name_phone_can_be_set',
            )
        ]

    def clean(self):
        """Ensure that only one of `user` and `email`, `first_name` etc. can be set."""
        if self.user and (self.email or self.first_name or self.last_name or self.phone):
            raise ValidationError('Only one of the fields can be set. (User or Email, First Name, Last Name, Phone)')

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_user_by_email(self):
        return get_user_model().objects.filter(email=self.email).first()

    def get_user_by_phone(self):
        return get_user_model().objects.filter(phone=self.phone, phone_extension=self.phone_extension).first()

    def __str__(self):
        return f'Message {self.user.get_full_name()} ({self.user.email})' if self.user else f'Message {self.get_full_name()} ({self.email})'
