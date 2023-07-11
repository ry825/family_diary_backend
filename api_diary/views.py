from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from api_diary import serializers
from core.models import Diary, Video, Picture
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.db.models import Q
import datetime
# Create your views here.


class DiaryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DiarySerializer
    queryset = Diary.objects.all()

    def list(self, request, *args, **kwargs):
        filter_param = request.GET.get('filter_param')
        user_id = request.GET.get('user_id')
        year = request.GET.get('year')
        month = request.GET.get('month')
        queryset = self.queryset

        if filter_param == 'false':
            dt_now = datetime.datetime.now()
            year = dt_now.year
            month = dt_now.month
            if (month == 1):
                previousMonth = 12
                nextMonth = 2
                previousYear = year - 1
                queryset = queryset.filter(
                    Q(year=year) & Q(month=month) & Q(user=user_id) | Q(year=previousYear) & Q(
                        month=previousMonth) & Q(user=user_id) | Q(year=year) & Q(month=nextMonth) & Q(user=user_id)
                )
            elif (month == 12):
                previousMonth = 11
                nextMonth = 1
                nextYear = year + 1
                queryset = queryset.filter(
                    Q(year=year) & Q(month=month) & Q(user=user_id) | Q(year=nextYear) & Q(
                        month=nextMonth) & Q(user=user_id) | Q(year=year) & Q(month=previousMonth) & Q(user=user_id)
                )
            else:
                previousMonth = month - 1
                nextMonth = month + 1
                queryset = queryset.filter(
                    Q(year=year) & Q(month=previousMonth) & Q(user=user_id) | Q(year=year) & Q(
                        month=month) & Q(user=user_id) | Q(year=year) & Q(month=nextMonth) & Q(user=user_id)
                )

        elif filter_param == 'true':
            if (int(month) == 1):
                previousMonth = 12
                nextMonth = 2
                previousYear = int(year) - 1
                queryset = queryset.filter(
                    Q(year=year) & Q(month=month) & Q(user=user_id) | Q(year=previousYear) & Q(
                        month=previousMonth) & Q(user=user_id) | Q(year=year) & Q(month=nextMonth) & Q(user=user_id)
                )
            elif (int(month) == 12):
                previousMonth = 11
                nextMonth = 1
                nextYear = int(year) + 1
                queryset = queryset.filter(
                    Q(year=year) & Q(month=month) & Q(user=user_id) | Q(year=nextYear) & Q(
                        month=nextMonth) & Q(user=user_id) | Q(year=year) & Q(month=previousMonth) & Q(user=user_id)
                )
            else:
                previousMonth = int(month) - 1
                nextMonth = int(month) + 1
                queryset = queryset.filter(
                    Q(year=year) & Q(month=previousMonth) & Q(user=user_id) | Q(year=year) & Q(
                        month=month) & Q(user=user_id) | Q(year=year) & Q(month=nextMonth) & Q(user=user_id)
                )

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = serializers.VideoSerializer
    lookup_field = 'pk'

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), dict):
            kwargs["many"] = True
        return super(VideoViewSet, self).get_serializer(*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        data_ids = request.data.get('ids', [])
        for data_id in data_ids:
            try:
                item = Video.objects.get(id=data_id)
                item.delete()
            except Video.DoesNotExist:
                pass
        return Response(status=204)


class PictureViewSet(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = serializers.PictureSerializer
    lookup_field = 'pk'

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), dict):
            kwargs["many"] = True
        return super(PictureViewSet, self).get_serializer(*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        data_ids = request.data.get('ids', [])
        for data_id in data_ids:
            try:
                item = Picture.objects.get(id=data_id)
                item.delete()
            except Picture.DoesNotExist:
                pass
        return Response(status=204)
