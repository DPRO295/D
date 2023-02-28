from django.db import models
from django.contrib.auth.models import User
# python manage.py makemigrations
# python manage.py migrate


# Create your models here.
class PostThread(models.Model):
    email = models.CharField(max_length=32)
    title = models.TextField(max_length=255)
    content = models.TextField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=32)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)


class User_liked_Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostThread, on_delete=models.CASCADE)


class BookMark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostThread, on_delete=models.CASCADE)
