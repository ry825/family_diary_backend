from rest_framework import serializers
from core.models import Diary, Video, Picture


class CreateVideoListSerializer(serializers.ListSerializer):

    def create(self, validated_data):
        diary_id = self.context['request'].data.get('diary')
        diary = Diary.objects.get(id=diary_id)
        videos = self.context['request'].FILES.getlist('video')
        created_videos = []

        for video in videos:
            new_video = Video(
                video=video, diary=diary
            )
            created_videos.append(new_video)
        Video.objects.bulk_create(created_videos)
        return created_videos


class VideoSerializer(serializers.ModelSerializer):
    diary = serializers.PrimaryKeyRelatedField(queryset=Diary.objects.all())

    class Meta:
        model = Video
        fields = ['id', 'video', 'diary']
        list_serializer_class = CreateVideoListSerializer


class CreatePictureListSerializer(serializers.ListSerializer):

    def create(self, validated_data):
        diary_id = self.context['request'].data.get('diary')
        diary = Diary.objects.get(id=diary_id)
        photos = self.context['request'].FILES.getlist('picture')
        print(photos)
        created_photos = []

        for photo in photos:
            new_photo = Picture(
                picture=photo, diary=diary
            )
            created_photos.append(new_photo)
        Picture.objects.bulk_create(created_photos)
        return created_photos


class PictureSerializer(serializers.ModelSerializer):
    diary = serializers.PrimaryKeyRelatedField(queryset=Diary.objects.all())

    class Meta:
        model = Picture
        fields = ['id', 'picture', 'diary']
        list_serializer_class = CreatePictureListSerializer


class DiarySerializer(serializers.ModelSerializer):
    related_video = VideoSerializer(many=True, read_only=True)
    related_picture = PictureSerializer(many=True, read_only=True)

    class Meta:
        model = Diary
        fields = ['id', 'title', 'journal', 'date',
                  'year', 'month', 'related_video', 'related_picture', 'user']
