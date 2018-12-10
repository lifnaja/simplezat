from django.db import models


class Rating(models.Model):
    sentiment = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        default='',
    )
    comment = models.TextField(
        null=False,
        blank=False,
        default='',
    )
