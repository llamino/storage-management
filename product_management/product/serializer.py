from rest_framework import serializers

from product.models import Product, Color, Size, Category, ProductRating

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['name']
class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class ProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRating
        fields = ['user', 'rating', 'pub_at']


class ProductSerializer(serializers.ModelSerializer):
    sizes = SizeSerializer(many=True)
    colors = ColorSerializer(many=True)
    ratings = ProductRatingSerializer(many=True)
    categories = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = ['name','image','description','stock','weight','score','price','sizes','colors','ratings','categories']


