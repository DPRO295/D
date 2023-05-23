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
from django.forms.models import model_to_dict
from django.forms import ModelForm
from django.db.models import Q

# ----------------------------------------  test use ----------------------------------------
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
# ----------------------------------------  test use ----------------------------------------


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect("/main_page/")
    else:
        return render(request, "home.html")


@csrf_protect
def main_page(request, thread_id=-1):
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
        if not request.user.is_authenticated:
            return render(request, "home.html")

        query = request.GET.get("search", "")       # if there is query get it otherwise blank
        user_obj = request.user.is_authenticated
        email = request.user.email
        uid = request.user.id
        staff_user = request.user.is_staff
        # print("staff_user", staff_user)
        # get and set the post thread data in reverse order by post dataf
        # post_thread_data = PostThread.objects.all().order_by("date").reverse()

        # if query:
        #     search_dic["content"] = query

        # TODO only search for the "content" part from "postthread" table for now
        all_thread = (PostThread.objects.filter(Q(content__contains=query) & Q(hided=0)).order_by("date").reverse()
                      | PostThread.objects.filter(Q(title__contains=query)&Q(hided=0)).order_by("date").reverse())
        for post in all_thread:
            is_liked = User_liked_Post.objects.filter(post=post, user=request.user).exists()
            is_disliked = User_disliked_Post.objects.filter(post=post, user=request.user).exists()
            post.is_liked = is_liked
            post.is_disliked = is_disliked

        return render(request, "main_page.html",
                      {"post_thread": all_thread, "check_login": user_obj, "user": request.user,
                       "staff_user": staff_user, "user_email": email, "username": request.user.username,
                       "query": query, "thread_id": thread_id})

    if request.method == "POST":
        # print(request.POST)
        # convert the POST queryset to list.
        post_kind_list = list(request.POST)     # <QueryDict: {'csrftoken':['token'],'post_name':['post_value'], ... ,}
        # print(post_kind_list)                 # ['csrftoken', 'post_value']
        post_kind = post_kind_list[1]           # so we can get the actual post kind from " post_kind_list[1] "
        print("post_kind", post_kind)
        # reset is same as all, can be removed
        if post_kind == "all" or post_kind == "resset":                    # if post kind is all no filter
            all_thread = PostThread.objects.filter(hided=0).order_by("date").reverse()
            all_annc = PostThread.objects.filter(category="announcement").order_by("date").reverse()
        else:                                                              # filter the posts with post_kind
            all_thread = PostThread.objects.filter(Q(category=post_kind) & Q(hided=0)).order_by("date").reverse()

        for post in all_thread:
            is_liked = User_liked_Post.objects.filter(post=post, user=request.user).exists()
            is_disliked = User_disliked_Post.objects.filter(post=post, user=request.user).exists()
            post.is_liked = is_liked
            post.is_disliked = is_disliked

        return render(request, "main_page.html",
                      {"post_thread": all_thread, "check_login": request.user.is_authenticated, "user": request.user,
                       "user_email": request.user.email,"username": request.user.username,"thread_id": thread_id})


# @csrf_exempt
# def show_thread(request):
#     # print(request.POST)                         # for debug use
#     thread_data = request.POST.dict()             # convert request POST to dict() type
#     # print(thread_data)
#     return HttpResponse(json.dumps(thread_data))   # dump the thread_data to json type
from django.core import serializers
@csrf_exempt
def show_thread(request):
    thread_id=request.POST.get('thread_id')
    thread_s=PostThread.objects.filter(id=thread_id)
    thread=thread_s.first()
    comments=thread.commentthread_set.all()
    thread_d=list(thread_s.values())[0]
    comments_d=list(comments.values())
    # thread_d = serializers.serialize('json', [thread])
    # comments_d = serializers.serialize('json', comments)
    # print(thread_d)
    post_user_name=User.objects.filter(id=thread.user.id).first().username
    thread_d['post_user_name']=post_user_name
    for comment_d in comments_d:
        user_name=User.objects.filter(id=comment_d['comment_user_id']).first().username
        comment_d['user_name']=user_name
    data={"thread":thread_d,"comments":comments_d}
    return JsonResponse(data)

@csrf_exempt
def tip_thread(request):
    thread_id=request.POST.get('thread_id')
    user_id=request.POST.get('user_id')
    tip_quantity=int(request.POST.get('tip_quantity'))

    thread=PostThread.objects.filter(id=thread_id).first()
    user=User.objects.filter(id=user_id).first()
    user_profile=UserProfile.objects.filter(user=user).first()

    thread.tip_num+=tip_quantity
    tip_num=thread.tip_num
    thread.save()
    user_profile.coins-=tip_quantity
    user_profile.save()
    CoinsLog.objects.create(user=request.user, credit_type="sub",
                            amount=tip_quantity)
    data={"tip_num":tip_num}
    return JsonResponse(data)

def course(request):
    if request.method == "GET":
        user_obj = request.user.is_authenticated
        email = request.user.email
        name = request.user.username
        return render(request, "course.html",
        {"check_login": user_obj, "user_email": email, "username": name, "user":request.user
                       })