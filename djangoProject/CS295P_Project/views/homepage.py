from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect
# from pymongo import MongoClient
import certifi

ca = certifi.where()
database_path = 'mongodb+srv://Dpropro:Dpropro@dpro.qls8nuc.mongodb.net/?retryWrites=true&w=majority'


# Create your views here.
def home(request):
    return render(request, "home.html")


def main_page(request):
    return render(request, "main_page.html")


def post_thread(request):
    return render(request, "post_thread.html")


def register(request):
    if request.method == "GET":
        return render(request, "signin.html")
    else:
        email = request.POST.get("email")
        password = request.POST.get("pwd")
        if User.objects.filter(username=email).exists():
            return render(request, "register.html", {"error_msg": "This email have been used."})
        User.objects.create_user(username=email, password=password)
        return render(request, "home.html")


@csrf_protect
def signin(request):
    if request.method == "GET":
        return render(request, "signin.html")
    else:
        email = request.POST.get("email")
        password = request.POST.get("pwd")
        user_obj = auth.authenticate(username=email, password=password)
        if user_obj:
            auth.login(request, user_obj)
            print(request.user)
            print(request.user.id)  # 1   check if the user already login
            print(request.user.username)
            print(request.user.is_active)  # True
            print(request.user.is_authenticated)  # True
            return render(request, "main_page.html",
                          {"check_login": user_obj,
                           "user_email": email,
                           "user_password": password, })
        else:
            return render(request, "signin.html")


# def signin(request):
#     if request.method == "GET":
#         return render(request, "signin.html")
#     else:
#         email = request.POST.get("email")
#         password = request.POST.get("pwd")
#
#         client = MongoClient(database_path, tlsCAFile=ca)
#         user = client["try"]["user"]
#         doc = list(user.find({"email": email}))
#         # user_obj = auth.authenticate(username=email, password=password)
#         client.close()
#         if doc == []:
#             return render(request, "signin.html", {"error_msg": "This email haven't been registered."})
#         elif doc[0]["pwd"] != password:
#             return render(request, "signin.html", {"error_msg": "Wrong password! Please try again."})
#         else:
#             # return HttpResponse("Sign in successfully!")            # login success
#             # ------------------ test use -------------------
#             # print(request.user)
#             # print(request.user.id)                # 1   check if the user already login
#             # print(request.user.username)
#             # print(request.user.is_active)         # True
#             # print(request.user.is_authenticated)  # True
#             # ------------------ test use --------------------
#             # auth.login(request, user_obj)
#             return render(request, "main_page.html")                  # if success jump to main_page
#
#
# def register(request):
#     if request.method == "GET":
#         return render(request, "register.html")
#     else:
#         email = request.POST.get("email")
#         password = request.POST.get("pwd")
#
#         client = MongoClient(database_path, tlsCAFile=ca)
#         user = client["try"]["user"]
#         doc = list(user.find({"email": email}))
#         if(doc != []):
#             client.close()
#             return render(request, "register.html", {"error_msg": "This email have been used."})
#         else:
#             user.insert_one({"email": email, "pwd": password})
#             client.close()
#             # User.objects.create_user(username=email, password=password)
#             # return HttpResponse("Register successfully!")
#             return render(request, "home.html")
