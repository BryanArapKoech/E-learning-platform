from django.shortcuts import render

# users/views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserRegisterSerializer, UserSerializer
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class UserRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (permissions.AllowAny,) # Anyone can register
    serializer_class = UserRegisterSerializer

# Optional: A view to get the current user's details
class CurrentUserView(generics.RetrieveAPIView):
     permission_classes = [permissions.IsAuthenticated]
     serializer_class = UserSerializer

     def get_object(self):
         return self.request.user

