from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token

from users import models, serializers


class UserRegisterApiView(generics.GenericAPIView):
    serializer_class = serializers.UserProfileSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        current_user = models.UserProfile.objects.get(email=serializer.data['email'])
        auth_token = RefreshToken.for_user(user).access_token
        return Response({
            'user_data': serializer.data,
            'message': 'User created successfully',
            'token' : str(auth_token)
        }, status=status.HTTP_201_CREATED)

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    # renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    serializer_class = serializers.LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        token = serializer.data['token']
        return Response({
            'token': token,
            'user_id': serializer.data['id'],
        }, status=status.HTTP_200_OK)
