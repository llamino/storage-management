from django.urls import path
from . import views
urlpatterns = [
    path('list/', views.WarehouseListView.as_view(), name='index'),
    path('detail/<slug:slug>/', views.WarehouseDetailView.as_view(), name='detail'),
    path('test/', views.test.as_view(), name='detail'),
]