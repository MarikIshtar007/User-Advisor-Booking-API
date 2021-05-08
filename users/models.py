from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):

    def create_user(self, email, name, password = None):
        if not email:
            raise ValueError("Users must have an email address")
        
        email = self.normalize_email(email)
        user = self.model(email = email, name=name)

        user.set_password(password)
        user.save(using = self._db)
        return user 
    
    def create_superuser(self, email, name, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_name(self):
        """Return full name of user"""
        return self.name
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {'refresh':str(refresh),
        'access':str(refresh.access_token)}

    def __str__(self):
        return self.email   


