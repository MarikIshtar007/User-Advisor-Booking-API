from django.shortcuts import render

from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from users import models
from users import serializers

class UserRegisterApiView(generics.GenericAPIView):
    serializer_class = serializers.UserProfileSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user': serializers.UserProfileSerializer(user, context=self.get_serializer_context()).data,
            'message': 'User created successfully. Now login to get your token'
        })

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


