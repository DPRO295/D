from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect
from CS295P_Project.models import *
from django.shortcuts import render, HttpResponse, redirect
from datetime import *
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

def teach_side(request):
    if request.method == "GET":
        # send login info
        user_obj = request.user.is_authenticated
        email = request.user.email
        return render(request, "teach_side.html",
                      {"check_login": user_obj, "user_email": email,
                       "username": request.user.username})