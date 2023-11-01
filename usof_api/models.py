from django.db import models
from django.conf import settings


# class Comment(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     publish_date = models.DateField()
#     content = models.TextField()
#
#     def __str__(self):
#         return self.author
#
#
# class Like(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     publish_date = models.DateField()
#     post_id = models.IntegerField()
#     comment_id = models.IntegerField()
#     type = models.BooleanField()
#
#     def __str__(self):
#         return self.author
