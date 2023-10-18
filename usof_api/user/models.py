from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    login = models.CharField("username", max_length=50, unique=True)
    email = models.EmailField("email", max_length=200)
    full_name = models.CharField("full_name", max_length=200, blank=True, null=True)
    picture = models.ImageField(upload_to="prof_pics", blank=True, null=True)
    rating = models.CharField("rating", max_length=200, blank=True, null=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "login"
    objects = UserManager()

    def __str__(self):
        return self.login
