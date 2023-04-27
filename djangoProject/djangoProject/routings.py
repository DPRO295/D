import sys
from django.urls import re_path
from django.urls import path
from . import consumers

# websocket的路由配置
websocket_urlpatterns = [
    re_path("^room/(?P<group>\w+)", consumers.ChatConsumer.as_asgi()),
    path("ws/post_reward/", consumers.MyConsumer.as_asgi()),
]