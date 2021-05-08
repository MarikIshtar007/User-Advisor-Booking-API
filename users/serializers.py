from rest_framework import serializers

from django.contrib import auth

from users import models

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a User Profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password' : {
                'write_only': True,
                'style' : {'input_type': 'password'}
            }
        }
    
    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password= validated_data['password']
        )
        return user

class LoginSerializer(serializers.ModelSerializer):
    """Serializer for login of user"""
    email=serializers.EmailField()
    password=serializers.CharField(max_length=64, write_only=True)
    token=serializers.CharField(read_only=True)

    class Meta:
        model= models.UserProfile
        fields = ['email','password','id','token']

    def validate(self, attrs):
        email=attrs.get('email','')
        password=attrs.get('password','')
        
        user=auth.authenticate(email=email,password=password)
        if not user:
            raise AuthenticationFailed('Invalid Credentials')
        
        return {
            'email':user.email,
            'token':user.tokens,
            'id':user.id
        }

