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
    form = UserModelForm
    return render(request, "test.html", {"form": form})


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
    print(request.user.id)
    print(request.user.username)
    print(request.user.email)
    print(request.user.is_active)  # True
    print(request.user.is_authenticated)
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
