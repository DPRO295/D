from django.db import models

# python manage.py makemigrations
# python manage.py migrate


# Create your models here.
class PostThread(models.Model):
    email = models.CharField(max_length=32)
    title = models.TextField(max_length=255)
    content = models.TextField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=32)

