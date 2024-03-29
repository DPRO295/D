from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect
from CS295P_Project.models import *
from datetime import *
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt


def post_thread(request):
    if request.method == "GET":
        # send login info
        user_obj = request.user.is_authenticated
        email = request.user.email
        post_threads = PostThread.objects.filter(hided=0)
        return render(request, "post_thread.html",
                      {"check_login": user_obj, "user_email": email,
                       "username": request.user.username, "post_threads": post_threads})
    # if it's a POST request
    user_id = request.user.id
    print(user_id)
    title = request.POST.get("title")
    content = request.POST.get("content")
    category = request.POST.get("category")
    PostThread.objects.create(title=title, content=content, category=category, user_id=user_id)
    return redirect("/main_page/")


def edit_thread(request, nid):
    if request.method == "GET":
        # send login info
        user_obj = request.user.is_authenticated
        # email = request.user.email
        # print(nid)
        thread_data = PostThread.objects.filter(id=nid).first()
        # print(thread_data.title, thread_data.content)
        return render(request, "edit_thread.html",
                      {"check_login": user_obj,
                       "username": request.user.username, "thread_data": thread_data}
                      )
    # if it's a POST request
    user = request.user.id
    title = request.POST.get("title")
    content = request.POST.get("content")
    category = request.POST.get("category")
    # have to manually update time even set to "auto_now=True", since calling update will not go through "models".
    # the "auto_now=True" will not be triggered
    PostThread.objects.filter(id=nid).update(title=title, content=content, user=user,
                                             category=category, date=datetime.now())
    return redirect("/main_page/"+str(nid))


def delete_post(request):
    if request.method == "GET":
        staff_user = request.user.is_staff
        user_id = request.user.id
        row_id = request.GET.get('nid')
        valid = PostThread.objects.filter(id=row_id, user_id=user_id).exists()

        # check if the user is staff_user or the valid user to delete the post
        if staff_user or valid:
            PostThread.objects.filter(id=row_id).delete()
        # TODO what if anyone force to delete the post
        else:
            print("!!!!!!!!!")
            return redirect("/main_page/")

    return redirect("/main_page/")


@csrf_exempt
def change_like(request, post_id, user_id, isliked):
    post = get_object_or_404(PostThread, id=post_id)
    user = get_object_or_404(User, id=user_id)
    # likeit = User_liked_Post.objects.filter(post=post, user=user)
    if isliked == 'True':
        # print("yes")
        post.likes -= 1
        post.save()
        # print(User_liked_Post.objects.filter(post=post, user=user).exists())
        User_liked_Post.objects.filter(post=post, user=user).delete()

    elif isliked == 'False':
        # print("No")
        post.likes += 1
        post.save()
        # print(User_liked_Post.objects.filter(post=post, user=user).exists())
        User_liked_Post.objects.create(post=post, user=user)

    data = {'likes': post.likes}
    return JsonResponse(data)


@csrf_exempt
def change_dislike(request, post_id, user_id, isdisliked):
    post = get_object_or_404(PostThread, id=post_id)
    user = get_object_or_404(User, id=user_id)
    # likeit = User_liked_Post.objects.filter(post=post, user=user)
    if isdisliked == 'True':
        # print("yes")
        post.dislikes -= 1
        post.save()
        # print(User_liked_Post.objects.filter(post=post, user=user).exists())
        User_disliked_Post.objects.filter(post=post, user=user).delete()

    elif isdisliked == 'False':
        # print("No")
        post.dislikes += 1
        post.save()
        # print(User_liked_Post.objects.filter(post=post, user=user).exists())
        User_disliked_Post.objects.create(post=post, user=user)

    data = {'dislikes': post.dislikes}
    return JsonResponse(data)