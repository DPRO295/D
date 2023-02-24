from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect
from CS295P_Project.models import *
from datetime import *


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect("/main_page/")
    else:
        return render(request, "home.html")


def main_page(request):
    # -------- test case -----------
    print("--- in main_page ---")
    print(request.user)
    print(request.user.id)  # 1   check if the user already login
    print(request.user.username)
    print(request.user.email)
    print(request.user.is_active)  # True
    print(request.user.is_authenticated)
    # -------- test case -----------

    # search_dic = {}
    query = request.GET.get("search", "")       # if there is query get it otherwise blank
    user_obj = request.user.is_authenticated
    email = request.user.email
    # get and set the post thread data in reverse order by post data
    # post_thread_data = PostThread.objects.all().order_by("date").reverse()

    # if query:
    #     search_dic["content"] = query

    # TODO only search for the "content" part from "postthread" table for now
    query_set = PostThread.objects.filter(content__contains=query).order_by("date").reverse()

    return render(request, "main_page.html",
                  {"post_thread": query_set, "check_login": user_obj, "user_email": email,
                   "username": request.user.username, "query": query})


def post_thread(request):
    if request.method == "GET":
        # send login info
        user_obj = request.user.is_authenticated
        email = request.user.email
        return render(request, "post_thread.html", {"check_login": user_obj, "user_email": email,
                                                    "username": request.user.username})
    # if it's a POST request
    email = request.user.email
    title = request.POST.get("title")
    content = request.POST.get("content")
    category = request.POST.get("category")
    PostThread.objects.create(title=title, content=content, email=email, category=category)
    return redirect("/main_page/")


def edit_thread(request, nid):
    if request.method == "GET":
        # send login info
        user_obj = request.user.is_authenticated
        email = request.user.email
        # print(nid)
        thread_data = PostThread.objects.filter(id=nid).first()
        # print(thread_data.title, thread_data.content)
        return render(request, "edit_thread.html",
                      {"check_login": user_obj, "user_email": email,
                       "username": request.user.username, "thread_data": thread_data}
                      )
    # if it's a POST request
    email = request.user.email
    title = request.POST.get("title")
    content = request.POST.get("content")
    category = request.POST.get("category")
    # have to manually update time even set to "auto_now=True", since calling update will not go through "models".
    # the "auto_now=True" will not be triggered
    PostThread.objects.filter(id=nid).update(title=title, content=content, email=email,
                                             category=category, date=datetime.now())
    return redirect("/main_page/")


def delete_post(request):
    row_id = request.GET.get('nid')
    PostThread.objects.filter(id=row_id).delete()
    return redirect("/main_page/")


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
        User.objects.create_user(username=username, email=email, password=password)
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


def profile(request):
    if request.method == "GET":
        user_obj = request.user.is_authenticated
        email = request.user.email
        name = request.user.username
        return render(request, "profile.html", {"check_login": user_obj, "user_email": email,
                                                "username": name, })
