from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    login = models.CharField("username", max_length=50, unique=True)
    email = models.EmailField("email", max_length=200)
    full_name = models.CharField("full_name", max_length=200, blank=True, null=True)
    picture = models.ImageField(upload_to="prof_pics", blank=True, null=True)
    rating = models.CharField("rating", max_length=200, blank=True, null=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "login"
    objects = UserManager()

    # @property
    # def is_staff(self):
    #     return self.is_staff

    def __str__(self):
        return self.login


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    publish_date = models.DateField(auto_now_add=True, blank=True, null=True)
    status = models.BooleanField()
    content = models.TextField(blank=True, null=True)
    categories = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    publish_date = models.DateField()
    content = models.TextField()

    def __str__(self):
        return self.author


class Like(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    publish_date = models.DateField()
    post_id = models.IntegerField()
    comment_id = models.IntegerField()
    type = models.BooleanField()

    def __str__(self):
        return self.author
