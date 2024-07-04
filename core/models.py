from django.db import models


# Create you
class QuoteRequest(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    service = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.service}"


class GeneralSetting(models.Model):
    name = models.CharField(
        default="",
        max_length=255,
        blank=True,

    )
    description = models.CharField(
        default='',
        max_length=255,
        blank=True,

    )
    parameter = models.CharField(
        default='',
        max_length=255,
        blank=True,
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        blank=True,

    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        blank=True,
    )
