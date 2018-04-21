from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def chatroom(request, room_name):
    print(request.user.username)
    if request.user.is_authenticated:
        return render(request, 'chatroom/chatroom.html', {'room_name': room_name})