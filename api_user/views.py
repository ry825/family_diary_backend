from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from api_user import serializers
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

class CreateUserView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny,)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    user = request.user
    # ユーザー情報を適切な形式でシリアライズする必要があります
    serializer = serializers.UserSerializer(user)

    return Response(serializer.data)