from django.urls import path
from .views import RegisterView, LoginView, ValidateJWTView, UserListCreateAPIView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('validate_jwt/', ValidateJWTView.as_view(), name='validate_jwt'),
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
]


# from django.urls import path
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
#
# app_name = 'authentication'
# urlpatterns = [
#     path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]
