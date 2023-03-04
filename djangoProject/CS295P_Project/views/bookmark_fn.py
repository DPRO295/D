from django.shortcuts import render, HttpResponse, redirect
from CS295P_Project.models import *
from django.shortcuts import get_object_or_404


def save_bookmark(request, post_id, user_id):
    post = get_object_or_404(PostThread, id=post_id)
    user = get_object_or_404(User, id=user_id)
    if BookMark.objects.filter(post=post, user=user):
        return redirect("/main_page/")
    else:
        BookMark.objects.create(post=post, user=user)
        return redirect("/main_page/")


def delete_bookmark(request, post_id):
    user = get_object_or_404(User, id=request.user.id)
    BookMark.objects.filter(post=post_id, user=user).delete()
    return redirect("/my_bookmark/")


def my_bookmark(request):
    if request.method == "GET":
        user_obj = request.user.is_authenticated
        email = request.user.email
        name = request.user.username
        # get all saved bookmarks id
        user_saved_bookmarks = BookMark.objects.filter(user_id=request.user.id)
        # store the id list
        id_list = [each_post_id.post_id for each_post_id in user_saved_bookmarks]
        # get all the actual post by using the id list
        display_bookmark = PostThread.objects.filter(id__in=id_list)
        # print(id_list)
        # print("display_bookmark",display_bookmark)
        return render(request, "my_bookmark.html",
                      {"check_login": user_obj, "user_email": email, "username": name,
                       "display_bookmark": display_bookmark})
