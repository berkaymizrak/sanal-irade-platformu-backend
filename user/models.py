from core.models import AbstractModel
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
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
    REQUIRED_FIELDS = ['birth_year', ]  # By doing so create superuser command will ask their input

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        db_table = 'auth_user'

    def __str__(self):
        return f'{self.get_full_name()} ({self.email})'
