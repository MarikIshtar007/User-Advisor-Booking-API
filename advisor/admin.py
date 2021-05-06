from django.contrib import admin

from .models import AdvisorProfile, Appointment
# Register your models here.
admin.site.register(AdvisorProfile)
admin.site.register(Appointment)
