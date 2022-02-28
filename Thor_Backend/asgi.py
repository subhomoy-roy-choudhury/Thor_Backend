"""
ASGI config for Thor_Backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os, sys
from pyngrok import ngrok
import pyrebase
from decouple import config
from urllib.parse import urlparse

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

# Ngrok Firestore Integration

addrport = urlparse("http://{}".format(sys.argv[-1]))
port = addrport.port if addrport.netloc and addrport.port else 8000

# bind_tls=True #for HTTPS
public_url = ngrok.connect(port).public_url
print("ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}\"".format(public_url, 8000))

firebaseConfig = {
      'apiKey': config('FIREBASE_API_KEY'),
      'authDomain': config('FIREBASE_AUTH_DOMAIN'),
      'databaseURL': config('FIREBASE_DATABASE_URL'),
      'projectId': config('FIREBASE_PROJECT_ID'),
      'storageBucket': config('FIREBASE_STORAGE_BUCKET'),
      'messagingSenderId': config('FIREBASE_MESSAGING_SENDER_ID'),
      'appId': config('FIREBASE_APP_ID'),
      'measurementId': config('FIREBASE_MEASUREMENT_ID')
 }

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

# jenna = db.child("ngrok-url").get()
# print(jenna.val())


db.update({"ngrok-url": public_url})