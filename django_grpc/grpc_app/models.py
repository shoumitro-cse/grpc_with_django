from django.db import models

# Create your models here.


class DataStorage(models.Model):
    iot_data = models.JSONField()

    class Meta:
        verbose_name = "Data Storage"
        verbose_name_plural = "Data Storages"
