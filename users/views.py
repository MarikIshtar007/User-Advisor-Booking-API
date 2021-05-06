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

class ShowAdvisors(generics.GenericAPIView):
    """Shows the list of all advisors"""
    serializer_class = serializers.AdvisorSerializer
    queryset = models.AdvisorProfile.objects.all()
    
    @action(methods=['get'], detail=True)
    def show_advisors(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many = True)
        return Response(serializer.data)

class AdvisorAddView(generics.GenericAPIView):
    """Used by admin to add Advisor"""
    serializer_class = serializers.AdvisorSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        advisor = serializer.save()
        return Response({
            'advisor': serializers.AdvisorSerializer(advisor, context=self.get_serializer_context()).data,
            'message': 'Advisor has been added successfully. No auth is used here as stated in the requirements..'
        })