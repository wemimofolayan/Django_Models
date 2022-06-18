import os
import django
import os 
import sys
from django.conf import settings
from django.db import models
from turtle import title
from django.contrib.auth import get_user_model

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.py'),

    django.setup()


User = settings.AUTH_USER_MODEL
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = author = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    created_date = models.DateTimeField()
    published_date = models.DateTimeField()

User = get_user_model