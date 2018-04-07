import datetime

from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.CharField(max_length=30, null=False)
    content = models.CharField(max_length=255, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today())

    def __str__(self):
        return "{} - {} ".format(self.pk, self.author)

class Comment(models.Model):
    content = models.CharField(max_length=255, null=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today())

    def __str__(self):
        return "{} - {} ".format(self.pk, self.post.author)