from django.db import models


# Create your models here.
class Like(models.Model):
    author = models.CharField(max_length=100)
    publish_date = models.DateField(auto_now_add=True, blank=True, null=True)
    post_id = models.IntegerField(null=True, blank=True)
    comment_id = models.IntegerField(null=True, blank=True)
    type = models.BooleanField(null=False, blank=False)
