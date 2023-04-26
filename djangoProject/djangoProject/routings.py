import sys
from django.urls import re_path
from . import consumers

# websocket的路由配置
websocket_urlpatterns = [
    re_path("^room/(?P<group>\w+)", consumers.ChatConsumer.as_asgi()),
]