from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect
from CS295P_Project.models import *
from datetime import *
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt


def profile(request):
    if request.method == "GET":
        user_obj = request.user.is_authenticated
        email = request.user.email
        name = request.user.username
        user_obj2 = request.user
        credit_obj = UserProfile.objects.filter(user=user_obj2).first()
        school_tmp = "None"
        birthday_tmp = "None"
        if credit_obj is not None:
            return render(request, "profile_update.html",
                      {"check_login": user_obj,
                       "user_email": email,
                        "username": name,
                       "credit": credit_obj.coins,
                       "birthday":birthday_tmp,
                       "school":school_tmp,})
        else:
            return render(request, "profile_update.html",
                          {"check_login": user_obj,
                           "user_email": email,
                           "username": name,
                           "credit": 0,
                           "birthday": birthday_tmp,
                           "school": school_tmp, })
    if request.method == "POST":
        if 'change_pwd' in request.POST:
            return redirect("/reset_pwd/")


def coins_page(request):
    user_obj = request.user.is_authenticated
    email = request.user.email
    if request.method == "GET":
        return render(request, "coins.html", {"check_login": user_obj, "user_email": email,
                                              "username": request.user.username})
    if request.method == 'POST':
        coins = request.POST['coins']
        if 'add' in request.POST:
            print("+", coins)
        elif 'subtract' in request.POST:
            print("-", coins)
        return render(request, "coins.html", {"check_login": user_obj})
