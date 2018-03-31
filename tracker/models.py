import datetime

from django.contrib.auth.models import User, AbstractUser
from django.db import models


class Entry (models.Model):
    date = models.DateField(default=datetime.date.today)
    distance = models.FloatField(max_length=15)
    time = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='', null=True)

    def __str__(self):
        return '{} - {}'.format(self.user, self.date)

    def get_absolute_url(self):
        return '/add/'


class ProfilePic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='', null=True)

    def __str__(self):
        return self.user.username