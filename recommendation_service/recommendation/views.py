# from .models import Warehouse
from .models_mongo import OrderRecommendationHistory, InteractionType, InteractionTypePerUser
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrderRecommendationHistorySerializer, InteractionTypePerUserSerializer, InteractionTypeSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnl

class test(APIView):
    def get(self, request):
        x = OrderRecommendationHistory(
            recommendation_product_id= "chips",
            user_id = "2",
            recommendation_date = datetime.now(),
            was_purchased = True,
        )
        x.save()
        y = InteractionType(
            title = "washing",
            description = "cleane all warehouses",
        )
        y.save()
        z = InteractionTypePerUser(
            interaction_type = "cleaning",
            user_id = "2",
            product_id = "chips",
            interaction_date = datetime.now(),
        )
        z.save()
        instance1 = InteractionType.objects.all()
        serializer1 = InteractionTypeSerializer(instance=instance1, many=True)
        instance2 = OrderRecommendationHistory.objects.all()
        serializer2 = OrderRecommendationHistorySerializer(instance=instance2, many=True)
        instance3 = InteractionTypePerUser.objects.all()
        serializer3 = InteractionTypePerUserSerializer(instance=instance3, many=True)
        return Response(data=serializer1.data,status=status.HTTP_201_CREATED)