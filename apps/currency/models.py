from django.db import models
from django.contrib.postgres.indexes import BrinIndex


class Currency(models.Model):
    name = models.CharField(
        max_length=5,
        null=True,
        blank=True,
        verbose_name="Name of currency"
    )
    rate = models.FloatField(
        null=True,
        blank=True,
        db_index=False,
        verbose_name="Currency rate to KZT",
    )
    published_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Date of publish"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'
        indexes = (
            BrinIndex(fields=['published_date']),
        )
