from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.conf import settings

from .managers import UserManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    login = models.CharField("username", max_length=50, unique=True)
    USERNAME_FIELD = "login"
    full_name = models.CharField("full_name", max_length=200)
    email = models.CharField("email", max_length=200)
    picture = models.ImageField(upload_to="prof_pics")
    rating = models.CharField("rating", max_length=200)
    objects = UserManager()

    def __str__(self):
        return self.login


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    publish_date = models.DateField()
    status = models.BooleanField()
    content = models.TextField()
    categories = models.CharField(max_length=50)

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
