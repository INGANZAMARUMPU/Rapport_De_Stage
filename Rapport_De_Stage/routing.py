from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from django.urls import path
from django.conf.urls import url
from apps.base.consumers import MainConsumer

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            	url(r"^service*", MainConsumer),
            ]
        )
    ),
})