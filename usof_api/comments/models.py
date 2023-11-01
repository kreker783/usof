from django.db import models
from usof_api.user.models import User


# Create your models here.
class Comment(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateField()
    content = models.TextField()

    def __str__(self):
        return self.author