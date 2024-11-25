from django.urls import path
from . import views
urlpatterns = [
    path('test', views.test.as_view(), name='test'),
]