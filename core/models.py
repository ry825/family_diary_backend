from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid
from django.conf import settings


def load_path_videos(instance, filename):
    return '/'.join(['videos', str(filename)])


def load_path_pictures(instance, filename):
    return '/'.join(['pictures', str(filename)])


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError('email is must')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.EmailField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email


class schedule(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, default=None)
    summary = models.CharField(max_length=20, blank=False)
    description = models.CharField(max_length=100, blank=False)
    start_time = models.DateTimeField(help_text='開始時間')
    end_time = models.DateTimeField(help_text='終了時間')


class Diary(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, default=None, related_name='related_diary')
    title = models.CharField(max_length=30)
    journal = models.CharField(max_length=500)
    date = models.CharField(max_length=15)
    year = models.IntegerField()
    month = models.IntegerField()

    def __str__(self):
        return self.title


class Picture(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    picture = models.ImageField(
        blank=False, upload_to=load_path_pictures)
    diary = models.ForeignKey(
        Diary, on_delete=models.CASCADE, default=None, related_name='related_picture')

    def __str__(self):
        return self.diary.title


class Video(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    video = models.FileField(
        blank=False, upload_to=load_path_videos)
    diary = models.ForeignKey(
        Diary, on_delete=models.CASCADE, default=None, related_name='related_video')

    def __str__(self):
        return self.diary.title
