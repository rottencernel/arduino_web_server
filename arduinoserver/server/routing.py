from django.urls import re_path, path

from . import consumers

websocket_urlpatterns = [
   re_path(r"a", consumers.ArduinoConsumer.as_asgi()),
]