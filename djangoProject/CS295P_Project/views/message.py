from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect
from CS295P_Project.models import *
from datetime import *
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from django.db.models import Count

def message_list(request):
    if request.method == "GET":
        user_obj = request.user.is_authenticated
        user_history_list = History.objects.filter(user=request.user)

        return render(request, 'message.html', {'user_history_list': user_history_list, "check_login": user_obj,
                                                "user_email": request.user.email,
                                                "username": request.user.username,
                                                })