from django.urls import path, include
from .views import ScheduleViewSet


urlpatterns = [
    path('', ScheduleViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='schedule_list'),

    path('<str:pk>/', ScheduleViewSet.as_view({
        'get': 'retrieve',
        'delete': 'destroy',
        'patch': 'partial_update',
    }), name='schedule_detail')
]
