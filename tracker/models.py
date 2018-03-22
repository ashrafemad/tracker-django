import datetime

from django.contrib.auth.models import User
from django.db import models


class Entry (models.Model):
    date = models.DateField(default=datetime.date.today)
    distance = models.FloatField(max_length=15)
    time = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.user, self.date)

    def get_absolute_url(self):
        return '/entries/'

