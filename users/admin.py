from django.contrib import admin

from .models import UserProfile
# Register your models here.
# Super-user credential is:
# username = Aster
# email = aster@gmail.com
# password = 12345

admin.site.register(UserProfile)
