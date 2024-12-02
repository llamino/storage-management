from datetime import timezone
import requests
from rest_framework import serializers
from .models import CategoryDiscount, ProductDiscount, UserDiscount
class CategoryDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryDiscount
        fields = '__all__'

class ProductDiscountSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = ProductDiscount
        fields = '__all__'

    def validate_product_id(self, product_id):
        # استفاده از آدرس داخلی برای بررسی محصول
        response = requests.get(f"http://localhost:9000/products/{product_id}")
        if response.status_code != 200:
            raise serializers.ValidationError("Invalid product ID.")
        return product_id

    def create(self, validated_data):
        validated_data['created_at'] = timezone.now()
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # for attr, value in validated_data.items():
        #     setattr(instance, attr, value)
        instance.updated_at = timezone.now()
        instance.save()
        return instance
class UserDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDiscount
        fields = '__all__'
