import datetime

# from django.contrib.gis.geos import Point
from django.db import models
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField
from ckeditor.fields import RichTextField
from stdimage import StdImageField


class Post(models.Model):
    author = models.CharField(max_length=30, null=False)
    content = models.CharField(max_length=255, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today())
    TYPES = (
        ('landcare', 'Landcare'),
        ('office', 'LLS Office'),
    )
    type = models.CharField(max_length=50, choices=TYPES, null=False, default='landcare')
    city = models.CharField(max_length=255, default='Cairo')
    location = PlainLocationField(based_fields=['city'], zoom=7)
    description = RichTextField()
    image = StdImageField(upload_to='images/', blank=True,
                          variations={
                              'large': (600, 400),
                              'thumbnail': (100, 100, True),
                              'medium': (300, 200),
                          })

    def __str__(self):
        return "{} - {} ".format(self.pk, self.author)



class Comment(models.Model):
    content = models.CharField(max_length=255, null=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today())

    def __str__(self):
        return "{} - {} ".format(self.pk, self.post.author)