from rest_framework import serializers

from advisor import models

class AdvisorSerializer(serializers.ModelSerializer):
    """Serializes an Advisor Profile object"""
    class Meta:
        model = models.AdvisorProfile
        fields = ('id', 'name', 'photo_url')
    

class AppointmentSerializer(serializers.ModelSerializer):
    """Serializes the Appointment Serializers"""

    class Meta:
        model = models.Appointment
        fields = ('user_id', 'advisor_id', 'booked_time')

    def create(self, validated_data):
        return models.Appointment.objects.create(**validated_data)


class ShowAppointmentSerializer(serializers.ModelSerializer):
    advisor_id = AdvisorSerializer()
    class Meta:
        model = models.Appointment
        fields = ('user_id', 'advisor_id', 'booked_time')
