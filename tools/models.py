from core.models import AbstractModel
from core.utils import get_translation
from django.db import models
from django.utils.translation import gettext_lazy as _
from tools import enums
from parler.models import TranslatableModel, TranslatedFields


# Create your models here.

class City(TranslatableModel, AbstractModel):
    translations = TranslatedFields(
        name=models.CharField(
            max_length=255,
            verbose_name=_('Name'),
        ),
    )
    code = models.CharField(
        max_length=5,
        verbose_name=_('Code'),
    )

    class Meta:
        ordering = ('translations__name',)
        verbose_name = _('City')
        verbose_name_plural = _('Cities')

    def __str__(self):
        return get_translation(self, 'name')


class Town(TranslatableModel, AbstractModel):
    translations = TranslatedFields(
        name=models.CharField(
            max_length=255,
            verbose_name=_('Name'),
        ),
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        verbose_name=_('City'),
    )

    class Meta:
        ordering = ('translations__name',)
        verbose_name = _('Town')
        verbose_name_plural = _('Towns')

    def __str__(self):
        return f'{get_translation(self, "name")} - {self.city}'


class District(TranslatableModel, AbstractModel):
    translations = TranslatedFields(
        name=models.CharField(
            max_length=255,
            verbose_name=_('Name'),
        ),
    )
    postal_code = models.CharField(
        default='',
        blank=True,
        max_length=5,
        verbose_name=_('Postal code'),
    )
    town = models.ForeignKey(
        Town,
        on_delete=models.CASCADE,
        verbose_name=_('Town'),
    )

    class Meta:
        ordering = ('translations__name',)
        verbose_name = _('District')
        verbose_name_plural = _('Districts')

    def __str__(self):
        return f'{get_translation(self, "name")} - {self.town}'


class SocialMedia(AbstractModel):
    order = models.IntegerField(
        default=10,
        verbose_name=_('Order'),
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
        verbose_name = _('Social Media')
        verbose_name_plural = _('Social Media Links')

    def __str__(self):
        return self.get_icon_display()
