from django.urls import path

from . import consumers

load_previous = [

    path('ws/chat/<roomName>/loadprevious/', consumers.loadprevious)
]