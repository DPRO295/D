import json

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect
from CS295P_Project.models import *
from datetime import *
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt


def get_reward_history(request):
    if request.method == "GET":
        # send login info
        user_obj = request.user.is_authenticated
        email = request.user.email
        user = request.user
        completed_question = PostThread.objects.filter(user=user).values('category', 'title', 'content')
        uncompleted_question = PostReward.objects.filter(user=user, is_completed=False).values('category', 'title', 'content')
        pending_answer = AnswerReward.objects.filter(answer_user = user, is_satisfied = False).values('content')

        data = {
                       'unfinished_questions': list(uncompleted_question)
                       ,'finished_questions': list(completed_question)
                        ,'pending_answer': list(pending_answer)
        }
        context = {
            "check_login": user_obj, "user_email": email,
            "username": request.user.username,
            'data': json.dumps(data),
        }
        return render(request, "reward_history.html",
                      context)