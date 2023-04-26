"""
ASGI config for djangoProject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
import django
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
django.setup()


from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from . import routings

# application = get_asgi_application()  # 注释掉原来的application

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),     # http走Django默认的asgi
        "websocket": AuthMiddlewareStack(
            URLRouter(
                routings.websocket_urlpatterns
            )
        ),
    }
)