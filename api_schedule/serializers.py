from rest_framework import serializers
from core.models import schedule


class ScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = schedule
        fields = ('id', 'summary', 'description', 'start_time', 'end_time', 'user')
