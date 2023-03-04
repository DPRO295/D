from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect
from CS295P_Project.models import *


def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    else:
        if request.POST.get("username") is None:
            return render(request, "register.html", {"error_msg": "please enter your username"})
        username = request.POST.get("username")
        print(username)
        email = request.POST.get("email")
        password = request.POST.get("pwd")
        if User.objects.filter(email=email).exists():
            return render(request, "register.html", {"error_msg": "This email have been used."})
        elif User.objects.filter(username=username).exists():
            return render(request, "register.html", {"error_msg": "This username have been used."})
        user = User.objects.create_user(username=username, email=email, password=password)
        user_profile = UserProfile(user=user, coins = 1000)
        user_profile.save()
        return redirect("/home/")


@csrf_protect
def signin(request):
    if request.method == "GET":
        return render(request, "signin.html")
    else:
        # TODO username CompareNoCase may cause problem
        username = request.POST.get("username")
        password = request.POST.get("pwd")
        user_obj = auth.authenticate(username=username, password=password)
        print(user_obj)
        if user_obj:
            # if login successfully set the session
            auth.login(request, user_obj)
            return redirect("/home/")
        else:
            return render(request, "signin.html", {"error_msg": "Wrong username or password"})


def logout(request):
    auth.logout(request)
    return redirect("/home/")


def reset_pwd(request):
    if request.method == "GET":
        user_obj = request.user.is_authenticated
        email = request.user.email
        return render(request, "reset_pwd.html", {"check_login": user_obj, "user_email": email,
                                                  "username": request.user.username})

    old_pwd = request.POST.get("old_pwd")
    new_pwd = request.POST.get("new_pwd")
    rnew_pwd = request.POST.get("rnew_pwd")

    if request.user.check_password(old_pwd):
        if new_pwd != rnew_pwd:
            return render(request, "reset_pwd.html", {"error_msg": "Entered passwords differ"})
        else:
            request.user.set_password(new_pwd)
            request.user.save()
            return redirect("/home/")
    return render(request, "reset_pwd.html", {"error_msg": "Entered wrong old password"})