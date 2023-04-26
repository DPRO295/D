"""
ASGI config for djangoProject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from . import routings      # 这个文件后续会说，你先写上。

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatroom.settings')
# application = get_asgi_application()  # 注释掉原来的application

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),     # http走Django默认的asgi
        "websocket": URLRouter(routings.websocket_urlpatterns),         # websocket走channels
    }
)