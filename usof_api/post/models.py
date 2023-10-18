from django.db import models
from django.conf import settings


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    publish_date = models.DateField(auto_now_add=True, blank=True, null=True)
    status = models.BooleanField()
    content = models.TextField(blank=True, null=True)
    categories = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title
