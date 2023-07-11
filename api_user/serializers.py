from django.contrib.auth import get_user_model
from rest_framework import serializers
from api_diary.serializers import DiarySerializer


class UserSerializer(serializers.ModelSerializer):
    related_diary = DiarySerializer(many=True, read_only=True)
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'related_diary')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)

        return user
