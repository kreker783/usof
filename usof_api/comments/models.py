from django.db import models
from django.conf import settings
from usof_api.post.models import Post


# Create your models here.
class Comment(models.Model):
    author = models.CharField(max_length=100)
    publish_date = models.DateField(auto_now_add=True, blank=True, null=True)
    content = models.TextField()
    post_id = models.ForeignKey(Post, on_delete=models.PROTECT)

    def __str__(self):
        return self.author