import datetime
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from api.models import Post


class PostSerializer(ModelSerializer):
    last_modified = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['author', 'content', 'date', 'user', 'last_modified']

    def get_last_modified(self, obj):

        return datetime.datetime.today().strftime('%d, %b %Y - %I:%M:%S')
