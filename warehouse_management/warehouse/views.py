from django.http import HttpResponse
from django.shortcuts import render

from .models import Warehouse
from .models_mongo import SupplierAndWarehouseTransaction
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from .models import Product
from .serializers import WarehouseSerializer, SupplierAndWarehouseTransactionSerializer
# from .tasks import update_inventory


class test(APIView):
    def get(self, request):
        x = SupplierAndWarehouseTransaction(
            supplier_id="1777",
            warehouse_id="1",
            product_id="1",
            quantity_supplied= 4,
            supply_price = 5.0,
            sale_price = 2.7,
            supplied_date =datetime(2020,2,4),
        )
        x.save()
        instance = SupplierAndWarehouseTransaction.objects.all()
        serializer = SupplierAndWarehouseTransactionSerializer(instance, many=True)
        return Response(data=serializer.data)
class WarehouseListView(APIView):
    def get(self, request):
        warehouses = Warehouse.objects.all()
        serializer = WarehouseSerializer(warehouses, many=True)
        return Response(serializer.data)
class WarehouseDetailView(APIView):
    def get(self, request, slug):
        warehouse = Warehouse.objects.get(slug=slug)
        serializer = WarehouseSerializer(warehouse)

        return Response(serializer.data)







# Create your views here.
