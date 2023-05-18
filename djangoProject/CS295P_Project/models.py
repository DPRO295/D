from django.db import models
from django.contrib.auth.models import User
from math import pow
# python manage.py makemigrations
# python manage.py migrate


# Create your models here.
class PostThread(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    taken_user_id = models.IntegerField(default=0)
    title = models.TextField(max_length=255)
    content = models.TextField(max_length=255)
    date = models.DateTimeField()
    category = models.CharField(max_length=32)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    tip_num = models.IntegerField(default=0)
    hided = models.IntegerField(default=0)


class CommentThread(models.Model):
    comment_user=models.ForeignKey(User, on_delete=models.CASCADE)
    thread=models.ForeignKey(PostThread, on_delete=models.CASCADE)
    content = models.TextField(max_length=pow(2, 15))
    date = models.DateTimeField()

class PostReward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=255)
    content = models.TextField(max_length=pow(2,15))
    date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=32)
    coin_num = models.IntegerField(default=0)
    is_taken = models.BooleanField(default=False)
    taken_user_id = models.IntegerField(default=0)
    is_completed = models.BooleanField(default=False)
    watches = models.IntegerField(default=0)


class AnswerReward(models.Model):
    answer_user = models.ForeignKey(User, on_delete=models.CASCADE)
    reward = models.ForeignKey(PostReward, on_delete=models.CASCADE)
    content = models.TextField(max_length=pow(2,15))
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    is_satisfied = models.BooleanField(default=False)

class User_liked_Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostThread, on_delete=models.CASCADE)

class User_disliked_Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostThread, on_delete=models.CASCADE)

class User_watched_Reward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reward = models.ForeignKey(PostReward, on_delete=models.CASCADE)

class BookMark_Thread(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostThread, on_delete=models.CASCADE)

class BookMark_Reward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostReward, on_delete=models.CASCADE)

class Replies(models.Model):
    parent_reply_id = models.IntegerField()
    comment_id = models.IntegerField()
    reply_content = models.CharField(max_length=255)
    reply_time = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    coins = models.IntegerField(default = 1000)

    def __str__(self):
        return f"{self.user} {self.coins}"

class CoinsLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    credit_type = models.CharField(max_length=10, choices=[('add', '增加'), ('sub', '减少')])
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    notes = models.CharField(max_length=100, blank=True, null=True)

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interact_id = models.TextField(null=True, blank=True)
    title = models.TextField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=32)
    coins_history = models.IntegerField(default=0)
    thread_id = models.IntegerField(null=True, blank=True)
