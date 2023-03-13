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
    coin_num = int(request.POST.get("coin_num"))

    user_profile=UserProfile.objects.filter(user=request.user).first()        # now let user's coins > reward coins by default
    user_profile.coins-=coin_num
    user_profile.save()
    PostReward.objects.create(title=title, content=content, user=request.user, category=category, coin_num=coin_num)
    return redirect("/current_rewards/")
