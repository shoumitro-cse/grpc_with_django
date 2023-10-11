from django.contrib import admin
from grpc_app.models import DataStorage


@admin.register(DataStorage)
class DataStorageAdmin(admin.ModelAdmin):
    list_display = ['id', 'iot_data']
    list_display_links = ['iot_data']
    search_fields = ['iot_data']