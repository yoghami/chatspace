from django.urls import path

from . import consumers

ChatConsumer = [
    path('ws/chat/<room_name>/', consumers.ChatConsumer),
    path('ws/chat/<roomName>/loadprevious/', consumers.loadprevious),
]

