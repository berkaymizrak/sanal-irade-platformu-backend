from core.models import AbstractModel
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models
from user.managers import *


# Create your models here.


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name='Email',
    )
    # TODO: Add role field
    identity_number = models.CharField(
        max_length=15,
        verbose_name='Identity number',
    )
    birth_year = models.PositiveSmallIntegerField(
        verbose_name='Birth year',
        validators=(MinValueValidator(1930), MaxValueValidator(2013),),
    )
    phone_extension = models.CharField(
        default='+90',
        max_length=6,
        verbose_name='Phone extension',
    )
    phone = models.CharField(
        max_length=15,
        verbose_name='Phone',
        validators=(RegexValidator(r'^\d{7,15}$'),),
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['birth_year', ]  # By doing so create superuser command will ask their input

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        db_table = 'auth_user'
