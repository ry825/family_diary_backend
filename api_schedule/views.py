from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from api_schedule import serializers
from core.models import schedule
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response
# Create your views here.


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = schedule.objects.all()
    serializer_class = serializers.ScheduleSerializer
