from django.db import models
from users.models import UserProfile

# Create your models here.
class AdvisorProfile(models.Model):
    """Model to store the Advisor Details"""
    name = models.CharField(max_length=255)
    photo_url = models.CharField(max_length = 255)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    """Table containing all the booked times between Advisors and Users"""
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE,related_name='appointments')
    advisor_id = models.ForeignKey(AdvisorProfile, on_delete=models.CASCADE)
    booked_time = models.DateTimeField()

    # Think of a proper str repr for this...
    # def __str__(self):
    #     return 