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
from django.utils import timezone

@csrf_protect
def current_rewards(request):
    if request.method == "GET":
        if not request.user.is_authenticated:
            return render(request, "home.html")

        reward_id = request.GET.get('reward_id')
        reward = PostReward.objects.filter(id=reward_id).first()

        query = request.GET.get("search", "")  # if there is query get it otherwise blank
        user_obj = request.user.is_authenticated
        email = request.user.email
        uid = request.user.id
        # get and set the post thread data in reverse order by post data
        # post_thread_data = PostThread.objects.all().order_by("date").reverse()

        # if query:
        #     search_dic["content"] = query

        # TODO only search for the "content" part from "postthread" table for now
        all_thread = (PostReward.objects.filter(content__contains=query)
                      | PostReward.objects.filter(title__contains=query)).order_by("date").reverse()
        for post in all_thread:
            is_watched = User_watched_Reward.objects.filter(reward=post, user=request.user).exists()
            post.is_watched = is_watched

        if reward:
            taken_user=User.objects.filter(id=reward.taken_user_id).first()         #if reward exists, give its taken user
            answers=AnswerReward.objects.filter(reward=reward).all()
        else:
            taken_user=None
            answers=None
        return render(request, "current_rewards.html",
                      {"post_thread": all_thread, "check_login": user_obj, "user": request.user,
                       "user_email": email,
                       "username": request.user.username, "query": query,"reward": reward,"taken_user":taken_user,
                       "answers":answers})

    if request.method == "POST":
        # print(request.POST)
        # convert the POST queryset to list.
        post_kind_list = list(request.POST)  # <QueryDict: {'csrftoken':['token'],'post_name':['post_value'], ... ,}
        # print(post_kind_list)                 # ['csrftoken', 'post_value']
        post_kind = post_kind_list[1]  # so we can get the actual post kind from " post_kind_list[1] "
        print("post_kind", post_kind)
        # reset is same as all, can be removed
        if post_kind == "all" or post_kind == "resset":  # if post kind is all no filter
            all_thread = PostReward.objects.order_by("date").reverse()
        else:  # filter the posts with post_kind
            all_thread = PostReward.objects.filter(category=post_kind).order_by("date").reverse()

        for post in all_thread:
            is_watched = User_watched_Reward.objects.filter(reward=post, user=request.user).exists()
            post.is_watched = is_watched

        # for post in all_thread:
        #     is_liked = User_liked_Post.objects.filter(post=post, user=request.user).exists()
        #     post.is_liked = is_liked

        return render(request, "current_rewards.html",
                      {"post_thread": all_thread, "check_login": request.user.is_authenticated,
                       "user": request.user,
                       "user_email": request.user.email, "username": request.user.username, })


@csrf_protect
def current_rewards2(request):
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
        # print(request.GET.get("general"))
        if not request.user.is_authenticated:
            return render(request, "home.html")
        query = request.GET.get("search", "")  # if there is query get it otherwise blank
        user_obj = request.user.is_authenticated
        email = request.user.email
        uid = request.user.id
        # get and set the post thread data in reverse order by post data
        # post_thread_data = PostThread.objects.all().order_by("date").reverse()

        # if query:
        #     search_dic["content"] = query

        # TODO only search for the "content" part from "postthread" table for now
        all_thread = (PostReward.objects.filter(content__contains=query)
                      | PostReward.objects.filter(title__contains=query)).order_by("date").reverse()
        for post in all_thread:
            is_watched = User_watched_Reward.objects.filter(reward=post, user=request.user).exists()
            post.is_watched = is_watched


        return render(request, "current_rewards.html",
                      {"post_thread": all_thread, "check_login": user_obj, "user": request.user,
                       "user_email": email,
                       "username": request.user.username, "query": query})

    if request.method == "POST":
        # print(request.POST)
        # convert the POST queryset to list.
        post_kind_list = list(request.POST)  # <QueryDict: {'csrftoken':['token'],'post_name':['post_value'], ... ,}
        # print(post_kind_list)                 # ['csrftoken', 'post_value']
        post_kind = post_kind_list[1]  # so we can get the actual post kind from " post_kind_list[1] "
        print("post_kind", post_kind)
        # reset is same as all, can be removed
        if post_kind == "all" or post_kind == "resset":  # if post kind is all no filter
            all_thread = PostReward.objects.order_by("date").reverse()
        else:  # filter the posts with post_kind
            all_thread = PostReward.objects.filter(category=post_kind).order_by("date").reverse()

        for post in all_thread:
            is_watched = User_watched_Reward.objects.filter(reward=post, user=request.user).exists()
            post.is_watched = is_watched

        # for post in all_thread:
        #     is_liked = User_liked_Post.objects.filter(post=post, user=request.user).exists()
        #     post.is_liked = is_liked

        return render(request, "current_rewards.html",
                      {"post_thread": all_thread, "check_login": request.user.is_authenticated,
                       "user": request.user,
                       "user_email": request.user.email, "username": request.user.username, })


@csrf_exempt
def show_reward(request):
    # print(request.POST)                         # for debug use
    thread_data = request.POST.dict()             # convert request POST to dict() type
    # print(thread_data)
    return HttpResponse(json.dumps(thread_data))   # dump the thread_data to json type


@csrf_exempt
def change_watch(request, post_id, user_id, iswatched):
    post = get_object_or_404(PostReward, id=post_id)
    user = get_object_or_404(User, id=user_id)
    # likeit = User_liked_Post.objects.filter(post=post, user=user)
    if iswatched == 'True':
        # print("yes")
        post.watches -= 1
        post.save()
        # print(User_liked_Post.objects.filter(post=post, user=user).exists())
        User_watched_Reward.objects.filter(reward=post, user=user).delete()

    elif iswatched == 'False':
        # print("No")
        post.watches += 1
        post.save()
        # print(User_liked_Post.objects.filter(post=post, user=user).exists())
        User_watched_Reward.objects.create(reward=post, user=user)

    data = {'watches': post.watches}
    return JsonResponse(data)


def edit_reward(request, nid):
    if request.method == "GET":
        # send login info
        user_obj = request.user.is_authenticated
        email = request.user.email
        # print(nid)
        thread_data = PostReward.objects.filter(id=nid).first()
        # print(thread_data.title, thread_data.content)
        return render(request, "edit_reward.html",
                      {"check_login": user_obj, "user_email": email,
                       "username": request.user.username, "thread_data": thread_data}
                      )
    # if it's a POST request
    user = request.user
    title = request.POST.get("title")
    content = request.POST.get("content")
    category = request.POST.get("category")
    # have to manually update time even set to "auto_now=True", since calling update will not go through "models".
    # the "auto_now=True" will not be triggered
    PostReward.objects.filter(id=nid).update(title=title, content=content, user=user,
                                             category=category, date=datetime.now())
    return redirect("/current_rewards/?reward_id="+str(nid))


def delete_reward(request):
    row_id = request.GET.get('nid')
    PostReward.objects.filter(id=row_id).delete()
    return redirect("/current_rewards/")

@csrf_exempt
def try_accept_reward(request):
    reward_id=request.POST.get('reward_id')
    want_user_id = request.POST.get('user_id')
    reward = PostReward.objects.filter(id=reward_id).first()
    post_user_id=reward.user.id

    if reward.is_taken:
        error_msg="Sorry that Someone has accepted this reward before you."
        status=0
    elif want_user_id==str(post_user_id):       # wrong

        error_msg="You cannot accept your own reward!"
        status=0
    else:                                   #success accept reward
        reward.taken_user_id=want_user_id
        reward.is_taken = True
        reward.save()
        error_msg=""
        status=1
    data={"error_msg":error_msg,"status":status}
    return JsonResponse(data)

@csrf_exempt
def add_reward_answer(request):
    text=request.POST.get('text')
    user_id=request.POST.get('user_id')
    reward_id=request.POST.get('reward_id')

    user=User.objects.filter(id=user_id).first()
    reward=PostReward.objects.filter(id=reward_id).first()
    AnswerReward.objects.create(answer_user=user,reward=reward,content=text)
    return HttpResponse()


@csrf_protect
def finish_reward(request):           # when poster is satisfied with the answer, the reward is deleted from Reward page and go to thread page
    reward_id = request.GET.get('reward_id')
    reward = PostReward.objects.filter(id=reward_id).first()

    taken_user=User.objects.filter(id=reward.taken_user_id).first()
    taken_user_profile = UserProfile.objects.filter(user=taken_user).first()
    taken_user_profile.coins+=reward.coin_num
    taken_user_profile.save()

    thread=PostThread.objects.create(user=reward.user,title=reward.title,content=reward.content
                              ,category=reward.category)
    answers=AnswerReward.objects.filter(reward=reward).all()
    for answer in answers:
        CommentThread.objects.create(comment_user=answer.answer_user,thread=thread,content=answer.content)
    reward.delete()
    return redirect("/current_rewards/")