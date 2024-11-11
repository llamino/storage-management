from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializer import ProductSerializer
from rest_framework.response import Response
from .models import ProductRating, Product
from rest_framework import status

class ProductDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, product_id):
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response({'eror': 'product does not exist'})
        product_serializer = ProductSerializer(product)
        return Response(data=product_serializer.data, status=status.HTTP_200_OK)

class ProductListView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        min_price = request.query_params.get('min_price', None)
        max_price = request.query_params.get('max_price', None)
        sizes = request.query_params.getlist('size')
        colors = request.query_params.getlist('color')
        category = request.query_params.get('category')
        in_stock = request.query_params.get('in_stock', None)
        products = Product.objects.all()
        if min_price is not None:
            products = products.filter(price__gte=min_price)
        if max_price is not None:
            products = products.filter(price__lte=max_price)
        if sizes:
            products = products.filter(size__in=sizes)
        if colors:
            products = products.filter(color__in=colors)
        if category:
            product = products.filter(category=category)
        if in_stock:
            products = products.filter(stock__gte=0)

        product_serializer = ProductSerializer(products, many=True)
        return Response(data=product_serializer.data, status=status.HTTP_200_OK)

class CreateProductRating(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, product_id):
        user_id = request.user.id  # استخراج user_id از توکن JWT
        rating = request.data.get('rating')
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        product_rating = ProductRating.objects.create(
            user_id=user_id,
            product=product,
            rating=rating
        )
        return Response({'message': 'Rating created successfully'}, status=status.HTTP_201_CREATED)

