from django.db import models
from django.conf import settings
from usof_api.categories.models import Category


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    publish_date = models.DateField(auto_now_add=True, blank=True, null=True)
    status = models.BooleanField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    categories = models.ManyToManyField(Category, null=True, blank=True)

    def __str__(self):
        return self.title
