from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
import json

# Create your views here.
@login_required
def chatroom(request, room_name):
    if request.user.is_authenticated:
        return render(request, 'chatroom/chatroom.html', context={'room_name': mark_safe(json.dumps(room_name))})

