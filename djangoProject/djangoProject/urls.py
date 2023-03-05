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
    path("reset_pwd/", views.reset_pwd),
    path("profile/", views.profile),

    # main_page functions:
    path("main_page/", views.main_page),
    path("coins/", views.coins_page),
    path("show_thread/", views.show_thread),

    # my_book_mark functions:
    path("my_bookmark/", views.my_bookmark),
    path("save_bookmark/<int:post_id>/<int:user_id>/", views.save_bookmark),
    path("delete_bookmark/<int:post_id>/", views.delete_bookmark),

    # post thread functions:
    path("post_thread/", views.post_thread),
    path("edit_thread/<int:nid>/", views.edit_thread),
    path("delete_post/", views.delete_post),
    path('change_like/<int:post_id>/<int:user_id>/<str:isliked>/', views.change_like, name='change_like'),

    # for test use
    path("test/", views.test),
]
