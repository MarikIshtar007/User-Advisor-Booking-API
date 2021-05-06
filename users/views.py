from django.shortcuts import render

from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserProfileSerializer

class UserRegisterApiView(generics.GenericAPIView):
    serializer_class = UserProfileSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user': UserProfileSerializer(user, context=self.get_serializer_context()).data,
            'message': 'User created successfully. Now login to get your token'
        })

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES