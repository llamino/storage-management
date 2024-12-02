from django.urls import path
from . import views
urlpatterns = [
    path('', views.SetDiscountForProduct.as_view(), name='set_discount_for_product'),
]