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
        user_history_list = History.objects.filter(user=request.user).order_by("date").reverse()

        return render(request, 'message.html', {'user_history_list': user_history_list, "check_login": user_obj,
                                                "user_email": request.user.email,
                                                "username": request.user.username,
                                                })
    if request.method == "POST":
        user_obj = request.user.is_authenticated
        post_kind_list = list(request.POST)
        post_kind = post_kind_list[1]
        # print("post_kind", post_kind)

        if post_kind == "all" or post_kind == "resset":  # if post kind is all no filter
            user_history_list = History.objects.filter(user=request.user).order_by("date").reverse()
        else:
            user_history_list = History.objects.filter(user=request.user, type=post_kind).order_by("date").reverse()

        return render(request, 'message.html', {'user_history_list': user_history_list, "check_login": user_obj,
                                                "user_email": request.user.email,
                                                "username": request.user.username,
                                                })


def del_mes_his(request):
    if request.method == "GET":
        staff_user = request.user.is_staff
        user_id = request.user.id
        row_id = request.GET.get('nid')
        valid = History.objects.filter(id=row_id, user_id=user_id).exists()

        # check if the user is staff_user or the valid user to delete the post
        if staff_user or valid:
            History.objects.filter(id=row_id).delete()
            print("deleted")
        # TODO what if anyone force to delete the post
        else:
            print("!!!!!!!!!")
            return redirect("/message_list/")

    return redirect("/message_list/")


def jump_message(request):
    message_id = request.GET.get('message_id')
    message = History.objects.filter(id=message_id).first()
    message.is_read = True
    message.save()

    reward = PostReward.objects.filter(id=message.thread_id).first()
    # print(message.thread_id)
    if not reward:
        thread_id = PostThread.objects.filter(reward_id=message.thread_id).first().id
        return redirect("/main_page/" + str(thread_id))
    else:
        return redirect("/current_rewards/" + str(reward.id))

@csrf_exempt
def update_message_box(request):
    read = (History.objects.filter(user=request.user, is_read=False).first()) is None
    data = {"read":read}
    return JsonResponse(data)