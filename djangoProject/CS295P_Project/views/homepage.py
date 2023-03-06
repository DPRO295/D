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

from django.forms import ModelForm


class UserModelForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]


def test(request):
    if request.method == "GET":
        user_obj = request.user.is_authenticated
        email = request.user.email
        form = UserModelForm
        return render(request, "test.html", {"check_login": user_obj, "user_email": email,
                                             "username": request.user.username, "form": form})
    if request.method == "POST":
        print(request.POST)
        # to deal with multiple post on pages
        # https://stackoverflow.com/questions/1395807/proper-way-to-handle-multiple-forms-on-one-page-in-django
        post_kind = request.POST.get("post")
        if post_kind == "post_1":
            print("yes")
            # return redirect("/main_page/")
            return render(request, "test.html", {"check_login": request.user.is_authenticated,
                                                 "user_email": request.user.email,
                                                 "username": request.user.username,
                                                 "which_post": post_kind})


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect("/main_page/")
    else:
        return render(request, "home.html")


def main_page(request):
    if request.method == "GET":
        # -------- test case -----------
        # print("--- in main_page ---")
        # print(request.user)
        # print(request.user.id)
        # print(request.user.username)
        # print(request.user.email)
        # print(request.user.is_active)  # True
        # print(request.user.is_authenticated)
        # -------- test case -----------

        # search_dic = {}
        query = request.GET.get("search", "")       # if there is query get it otherwise blank
        user_obj = request.user.is_authenticated
        email = request.user.email
        uid = request.user.id
        # get and set the post thread data in reverse order by post data
        # post_thread_data = PostThread.objects.all().order_by("date").reverse()

        # if query:
        #     search_dic["content"] = query

        # TODO only search for the "content" part from "postthread" table for now
        all_thread = PostThread.objects.filter(content__contains=query).order_by("date").reverse()
        for post in all_thread:
            is_liked = User_liked_Post.objects.filter(post=post, user=request.user).exists()
            post.is_liked = is_liked

        return render(request, "main_page.html",
                      {"post_thread": all_thread, "check_login": user_obj, "user": request.user,"user_email": email,
                       "username": request.user.username, "query": query})


@csrf_exempt
def show_thread(request):
    # print(request.POST)                         # for debug use
    thread_data = request.POST.dict()             # convert request POST to dict() type
    # print(thread_data)
    return HttpResponse(json.dumps(thread_data))   # dump the thread_data to json type
