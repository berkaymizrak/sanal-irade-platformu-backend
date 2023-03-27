from core.models import AbstractModel
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from tools.models import District
from user.managers import *


# Create your models here.


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name=_('Email'),
    )
    # TODO: Add role field
    identity_number = models.CharField(
        max_length=15,
        verbose_name=_('Identity number'),
    )
    birth_year = models.PositiveSmallIntegerField(
        verbose_name=_('Birth year'),
        validators=(MinValueValidator(1930), MaxValueValidator(2013),),
    )
    phone_extension = models.CharField(
        default='+90',
        max_length=6,
        verbose_name=_('Phone extension'),
    )
    phone = models.CharField(
        max_length=15,
        verbose_name=_('Phone'),
        validators=(RegexValidator(r'^\d{7,15}$'),),
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    # By doing below, create superuser command will ask their input:
    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'birth_year',
    ]

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        db_table = 'auth_user'

    def save(self, *args, **kwargs):
        is_new = self.id is None
        super(User, self).save(*args, **kwargs)
        if is_new:
            UserAuthorizedArea.objects.get_or_create(user=self)

    def __str__(self):
        return f'{self.get_full_name()} ({self.email})'


class UserAuthorizedArea(AbstractModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('User'),
        related_name='user_authorized_area',
    )
    district = models.ManyToManyField(
        District,
        default=None,
        blank=True,
        verbose_name=_('District'),
    )
    approved = models.BooleanField(
        default=False,
        verbose_name=_('Approved'),
    )

    class Meta:
        ordering = ('-created_date',)
        verbose_name = _('User Authorized Area')
        verbose_name_plural = _('User Authorized Areas')

    def save(self, *args, **kwargs):
        instance = UserAuthorizedArea.objects.filter(user=self.user)
        if len(instance):
            instance.delete()
        super(UserAuthorizedArea, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.user} - {self.district}'


class GDPRConsent(AbstractModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('User'),
    )
    agreement = models.CharField(
        max_length=255,
        verbose_name=_('Agreement'),
    )
    ip_address = models.GenericIPAddressField(
        verbose_name=_('IP address'),
    )
    is_accepted = models.BooleanField(
        default=False,
        verbose_name=_('Is accepted'),
    )

    class Meta:
        ordering = ('-created_date',)
        verbose_name = _('GDPR Consent')
        verbose_name_plural = _('GDPR Consents')

    def __str__(self):
        return f'{self.user} - {self.is_accepted}'
