from django.urls import path, include
from .views import DiaryViewSet, VideoViewSet, PictureViewSet


urlpatterns = [

    path('', DiaryViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='diary_list'),

    path('video/', VideoViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='video_list'),

    path('picture/', PictureViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='picture_list'),

    path('<str:pk>/',
         DiaryViewSet.as_view({
             'get': 'retrieve',
             'delete': 'destroy',
             'put': 'update',
         }), name='diary_detail'),
]
