from django.contrib import admin
from grpc_app.models import DataStorage, Customer


@admin.register(DataStorage)
class DataStorageAdmin(admin.ModelAdmin):
    list_display = ['id', 'iot_data']
    list_display_links = ['iot_data']
    search_fields = ['iot_data']


@admin.register(Customer)
class DataStorageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', "email"]
    list_display_links = ['name',]
    search_fields = ['name', "email"]