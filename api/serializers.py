import datetime
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from api.models import Post

from stdimage_serializer.fields import StdImageField


class PostSerializer(ModelSerializer):
    last_modified = serializers.SerializerMethodField()
    image = StdImageField()
    class Meta:
        model = Post
        fields = ['author', 'content', 'date', 'user', 'type', 'last_modified', 'city', 'location', 'description', 'image']

    def get_last_modified(self, obj):
        return datetime.datetime.today().strftime('%d, %b %Y - %I:%M:%S')
