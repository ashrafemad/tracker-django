from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView

from api.serializers import PostSerializer
from .models import Post, Comment

class ApiViewPosts(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ApiCreatePost(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
