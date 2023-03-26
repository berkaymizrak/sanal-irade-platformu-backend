from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


class AbstractModel(models.Model):
    updated_date = models.DateTimeField(
        verbose_name=_('Updated Date'),
        blank=True,
        auto_now=True,
    )
    created_date = models.DateTimeField(
        verbose_name=_('Created Date'),
        blank=True,
        auto_now_add=True,
    )

    class Meta:
        abstract = True
