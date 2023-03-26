from django.db import models


# Create your models here.


class AbstractModel(models.Model):
    updated_date = models.DateTimeField(
        verbose_name='Updated Date',
        blank=True,
        auto_now=True,
    )
    created_date = models.DateTimeField(
        verbose_name='Created Date',
        blank=True,
        auto_now_add=True,
    )

    class Meta:
        abstract = True
