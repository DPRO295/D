"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from CS295P_Project import views


# where to find the app
urlpatterns = [
    # path("admin/", admin.site.urls),
    # home page
    path('', views.home, name='home'),
    path("home/", views.home),

    # login system functions:
    path("signin/", views.signin),
    path("register/", views.register),
    path("logout/", views.logout),

    # profile page:
    path("reset_pwd/", views.reset_pwd),
    path("edit_email/", views.edit_email),
    path("edit_name/", views.edit_name),
    path("profile/", views.profile),

    # main_page functions:
    path("main_page/", views.main_page),
    path("main_page/<int:thread_id>", views.main_page),
    path("coins/", views.coins_page),
    path("show_thread/", views.show_thread),
    path("course/", views.course),

    # my_book_mark functions:
    path("my_bookmark_thread/", views.my_bookmark_thread),
    path("my_bookmark_reward/", views.my_bookmark_reward),
    path("save_bookmark_thread/<int:post_id>/<int:user_id>/", views.save_bookmark_thread),
    path("delete_bookmark_thread/<int:post_id>/", views.delete_bookmark_thread),
    path("save_bookmark_reward/<int:post_id>/<int:user_id>/", views.save_bookmark_reward),
    path("delete_bookmark_reward/<int:post_id>/", views.delete_bookmark_reward),

    # post thread functions:
    path("post_thread/", views.post_thread),
    path("edit_thread/<int:nid>/", views.edit_thread),
    path("delete_post/", views.delete_post),
    path('change_like/<int:post_id>/<int:user_id>/<str:isliked>/', views.change_like, name='change_like'),
    path('change_dislike/<int:post_id>/<int:user_id>/<str:isdisliked>/', views.change_dislike, name='change_dislike'),

    # message:
    path("message_list/", views.message_list),
    path("del_mes_his/", views.del_mes_his),
    path("jump_message/", views.jump_message),
    path("update_message_box/", views.update_message_box),
    # for test use
    path("test/", views.test),

    # reward
    path("response_reward/", views.res_reward),
    path("post_reward/",views.post_reward),
    # path("current_rewards/", views.current_rewards),
    path("current_rewards/", views.current_rewards),
    path("current_rewards/<int:reward_id>", views.current_rewards),

    path("show_reward/", views.show_reward),
    path("edit_reward/<int:nid>/", views.edit_reward),
    path("delete_reward/", views.delete_reward),
    path('change_watch/<int:post_id>/', views.change_watch, name='change_watch'),
    path('try_accept_reward/',views.try_accept_reward),
    path('add_reward_answer/',views.add_reward_answer),
    path('finish_reward/', views.finish_reward),
    path('tip_thread/',views.tip_thread),
    path('ans_history/', views.get_reward_history),
    path('teach_as/', views.teach_side),
]
