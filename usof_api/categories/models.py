from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100, unique=True, primary_key=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title
