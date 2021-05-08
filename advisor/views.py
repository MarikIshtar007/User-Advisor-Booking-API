from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, permissions, status

from advisor import serializers
from advisor import models

# Create your views here.
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


class ShowAdvisors(generics.ListAPIView):
    """Shows the list of all advisors"""
    serializer_class = serializers.AdvisorSerializer
    queryset = models.AdvisorProfile.objects.all()
    permission_classes = [permissions.IsAuthenticated]
 

    # def list(self, request):
    #     queryset = self.get_queryset()
    #     serializer = self.serializer_class(queryset, many = True)
    #     return Response(serializer.data)


class BookAdvisors(generics.GenericAPIView):
    """Adds appointments for users and advisor """
    serializer_class = serializers.AppointmentSerializer


    def post(self, request,user_id, advisor_id):
        usr = models.UserProfile.objects.get(id=user_id)
        adv = models.AdvisorProfile.objects.get(id=advisor_id)
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        appointment = serializer.save(user_id=usr, advisor_id=adv)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class ShowAppointments(generics.ListAPIView):
    """Shows the respective bookings made by the current user"""
    serializer_class = serializers.ShowAppointmentSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # Look into if this is possible with generic api and with a viewset....
    def get_queryset(self):
        return models.Appointment.objects.all()

    def get(self,request,user_id):
        user=models.UserProfile.objects.get(id=user_id)
        queryset=user.appointments.all()
        serializer = self.get_serializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)