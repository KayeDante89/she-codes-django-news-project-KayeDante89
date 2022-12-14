from django.contrib import admin
from .models import NewsStory, Comment

admin.site.register(NewsStory)
# Register your models here.
admin.site.register(Comment)
