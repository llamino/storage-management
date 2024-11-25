from rest_framework import serializers

class InteractionTypeSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()

class InteractionTypePerUserSerializer(serializers.Serializer):
    interaction_type = serializers.CharField()
    user_id = serializers.CharField()
    product_id = serializers.CharField()
    interaction_date = serializers.DateTimeField()

class OrderRecommendationHistorySerializer(serializers.Serializer):
    recommendation_product_id = serializers.CharField()
    user_id = serializers.CharField()
    recommendation_date = serializers.DateTimeField()
    was_purchased = serializers.BooleanField()
