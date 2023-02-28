from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect
from CS295P_Project.models import *
from datetime import *
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

def add_reply(request):
    comment_id = request.POST['comment_id']
    parent_reply_id = request.POST.get('parent_reply_id', None)
    reply_content = request.POST['reply_content']
    user_id = request.POST['user_id']
    reply = Replies(comment_id=comment_id, parent_reply_id=parent_reply_id, reply_content=reply_content, user_id=user_id)
    reply.save()
    return HttpResponse("Reply added successfully!")
