from django.urls import path, include
from api_user import views
from .views import get_user_info

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('info/', get_user_info, name='get_user_info'),
]