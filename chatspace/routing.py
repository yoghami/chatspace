from channels.routing import ProtocolTypeRouter
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chatroom.routing

application = ProtocolTypeRouter(
    {
        'websocket': AuthMiddlewareStack(
                URLRouter(
                    chatroom.routing.ChatConsumer
                )
            ),
    }
)