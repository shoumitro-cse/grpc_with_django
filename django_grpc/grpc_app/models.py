from django.db import models

# Create your models here.


class DataStorage(models.Model):
    iot_data = models.JSONField()

    class Meta:
        verbose_name = "Data Storage"
        verbose_name_plural = "Data Storages"


class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
