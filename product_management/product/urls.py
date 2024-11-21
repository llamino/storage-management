from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
# from .views import ProductViewSet

# ایجاد Router و ثبت ViewSet
# router = DefaultRouter()
# router.register(r'products', ProductViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('test', views.test.as_view(), name='test'),
]
