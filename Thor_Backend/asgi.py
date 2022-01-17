"""
ASGI config for Thor_Backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from script_builder.consumers import TestConsumer, NewConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Thor_Backend.settings')

application = get_asgi_application()

ws_pattern= [
    path('ws/home/',TestConsumer.as_asgi()),
    path('ws/new/' , NewConsumer.as_asgi())
]

application= ProtocolTypeRouter(
    {
        'websocket':URLRouter(ws_pattern)
    }
)