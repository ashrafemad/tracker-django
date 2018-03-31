from django.contrib import admin

# Register your models here.
from tracker.models import Entry, ProfilePic

admin.site.register(Entry)
admin.site.register(ProfilePic)

