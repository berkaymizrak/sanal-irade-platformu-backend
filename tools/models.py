from core.models import AbstractModel
from django.db import models
from django.utils.translation import gettext_lazy as _
from tools import enums


# Create your models here.

class City(AbstractModel):
    name = models.CharField(
        max_length=255,
        verbose_name=_('Name'),
    )
    code = models.CharField(
        max_length=5,
        verbose_name=_('Code'),
    )

    class Meta:
        ordering = ('name',)
        verbose_name = _('City')
        verbose_name_plural = _('Cities')

    def __str__(self):
        return self.name


class Town(AbstractModel):
    name = models.CharField(
        max_length=255,
        verbose_name=_('Name'),
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        verbose_name=_('City'),
    )

    class Meta:
        ordering = ('name',)
        verbose_name = _('Town')
        verbose_name_plural = _('Towns')

    def __str__(self):
        return self.name


class District(AbstractModel):
    name = models.CharField(
        max_length=255,
        verbose_name=_('Name'),
    )
    postal_code = models.CharField(
        max_length=5,
        verbose_name=_('Postal code'),
    )
    town = models.ForeignKey(
        Town,
        on_delete=models.CASCADE,
        verbose_name=_('Town'),
    )

    class Meta:
        ordering = ('name',)
        verbose_name = _('District')
        verbose_name_plural = _('Districts')

    def __str__(self):
        return self.name


class SocialMedia(AbstractModel):
    order = models.IntegerField(
        default=10,
        verbose_name=_('Order'),
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_('Name'),
    )
    url = models.URLField(
        verbose_name=_('URL'),
    )
    icon = models.CharField(
        verbose_name=_('Icon'),
        max_length=255,
        choices=enums.SocialMediaIcons.choices,
    )

    class Meta:
        ordering = ('order',)
        verbose_name = _('Social media')
        verbose_name_plural = _('Social media links')

    def __str__(self):
        return self.name
