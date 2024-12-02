from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from serializers import ProductDiscountSerializer, CategoryDiscountSerializer, UserDiscountSerializer
from . import models


class SetDiscountForProduct(APIView):
    def post(self, request):
        serializer = ProductDiscountSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DecreaseStockDiscountForProduct(APIView):
    def post(self, request):
        serializer = ProductDiscountSerializer(data=request.data)
        if serializer.is_valid():
            number = int(serializer.data['number'])
            serializer.stock = serializer.stock - number
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CheckDiscountForUserAndCategory(APIView):
    def post(self, request):