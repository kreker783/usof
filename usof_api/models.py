from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

from .managers import UserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    login = models.CharField("username", unique=True)
    USERNAME_FIELD = "login"
    objects = UserManager()

    def __str__(self):
        return self.login
