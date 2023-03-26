from core.models import AbstractModel
from django.db import models


# Create your models here.

class City(AbstractModel):
    name = models.CharField(
        max_length=255,
        verbose_name='Name',
    )
    code = models.CharField(
        max_length=5,
        verbose_name='Code',
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


class Town(AbstractModel):
    name = models.CharField(
        max_length=255,
        verbose_name='Name',
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        verbose_name='City',
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Town'
        verbose_name_plural = 'Towns'

    def __str__(self):
        return self.name


class District(AbstractModel):
    name = models.CharField(
        max_length=255,
        verbose_name='Name',
    )
    postal_code = models.CharField(
        max_length=5,
        verbose_name='Postal code',
    )
    town = models.ForeignKey(
        Town,
        on_delete=models.CASCADE,
        verbose_name='Town',
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'District'
        verbose_name_plural = 'Districts'

    def __str__(self):
        return self.name
