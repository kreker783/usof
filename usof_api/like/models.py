from django.db import models


# Create your models here.
class Like(models.Model):
    author = models.CharField(max_length=100)
    publish_date = models.DateField(auto_now_add=True, blank=True, null=True)
    post_id = models.IntegerField()
    comment_id = models.IntegerField()
    type = models.BooleanField(null=False, blank=False)
