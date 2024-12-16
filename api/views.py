from django.shortcuts import render
from rest_framework import generics  # helps us to create a class that inherits from a generic api view
from .serializers import RoomSerializer
from .models import Room

class RoomView(generics.ListAPIView):
    query = Room.objects.all()
    serializer_class = RoomSerializer

