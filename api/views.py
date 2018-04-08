from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from django.core.mail import send_mail
from api.serializers import PostSerializer
from .models import Post, Comment

class ApiViewPosts(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ApiCreatePost(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def post(self, request, *args, **kwargs):
    #     send_mail(
    #         'New Post Added',
    #         request.POST.get('content'),
    #         'from@example.com',
    #         ['ashrafemad23@gmail.com'],
    #         fail_silently=False,
    #     )
    #     return super().post(request, *args, **kwargs)

