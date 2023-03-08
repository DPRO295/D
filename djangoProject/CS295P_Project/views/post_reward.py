from django.shortcuts import render, HttpResponse, redirect
from CS295P_Project.models import *
def post_reward(request):
    if request.method == "GET":
        user_obj = request.user.is_authenticated
        Rewards = PostReward.objects.all()
        return render(request, "post_reward.html",
                      {"check_login": user_obj, "username": request.user.username,
                       "Rewards":Rewards,"user_id":request.user.id})

    email = request.user.email
    title = request.POST.get("title")
    content = request.POST.get("content")
    category = request.POST.get("category")
    coin_num = request.POST.get("coin_num")
    PostReward.objects.create(title=title, content=content, user_id=request.user.id, category=category, coin_num=coin_num)
    return redirect("/main_page/")
