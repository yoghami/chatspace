from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.utils.safestring import mark_safe
from index.models import Room
import json

# Create your views here.
@login_required
def chatroom(request, room_name):
    if request.user.is_authenticated:
        check_valid_user = Room.objects.filter(users=request.user, name=room_name).first()
        if check_valid_user:
            return render(request, 'chatroom/chatroom.html', context={'room_name': mark_safe(json.dumps(room_name))})


def log(request):
    logout(request)
    return redirect('index')