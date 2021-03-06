"""task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from tracker.views import Signup, Login, MyEntries, CreateEntry, index, signout, DeleteEntry, UpdateEntry, ListUsers, \
    DeleteUser, UpdateUser, validate_username

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('signup/', Signup.as_view(), name='signup'),
    path('validate/', validate_username, name='validate'),
    path('login/', Login.as_view(), name='login'),
    path('entries/', MyEntries.as_view(), name='entries'),
    path('add/', CreateEntry.as_view(), name='add'),
    path('entries/<int:pk>/delete', DeleteEntry.as_view(), name='delete-entry'),
    path('entries/<int:pk>/update', UpdateEntry.as_view(), name='update-entry'),
    path('index/', index, name='index'),
    path('logout/', signout, name='logout'),
    path('users/', ListUsers.as_view(), name='users-list'),
    path('users/<int:pk>/delete', DeleteUser.as_view(), name='delete-user'),
    path('users/<int:pk>/update', UpdateUser.as_view(), name='update-user'),
    path('api/posts/', include('api.urls'), name='api-posts-list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
