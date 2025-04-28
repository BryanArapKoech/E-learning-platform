# users/urls.py
from django.urls import path
from .views import UserRegisterView, CurrentUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('me/', CurrentUserView.as_view(), name='current_user'), # Endpoint to get current user details

    # Simple JWT URLs
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # Use this for login
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]