from django.utils.text import slugify
from rest_framework import serializers
from .models_mongo import SupplierAndWarehouseTransaction
from warehouse.models import Warehouse


class SupplierAndWarehouseTransactionSerializer(serializers.Serializer):
    supplier_id = serializers.CharField()
    warehouse_id = serializers.CharField()
    product_id = serializers.CharField()
    quantity_supplied = serializers.IntegerField()
    supply_price = serializers.FloatField()
    sale_price = serializers.FloatField()
    supplied_date = serializers.DateTimeField()

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'

    def create(self, validated_data):
        if 'slug' not in validated_data or not validated_data['slug']:
            validated_data['slug'] = slugify(validated_data['name'])
        return super().create(validated_data)
    def update(self, instance, validated_data):
        if 'name' in validated_data:
            validated_data['name'] = slugify(validated_data['name'])
        return super().create(validated_data)
