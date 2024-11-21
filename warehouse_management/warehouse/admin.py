from django.contrib import admin
from .models import Warehouse
@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'date_of_establishment', 'is_full')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('is_full',)

# Register your models here.
