from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout
from . forms import RoomForm, JoinForm
from index.views import valid_password
from index.models import Room
# Create your views here.


def start(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and 'create' in request.POST:
            form = RoomForm(request.POST)
            if form.is_valid():
                error = valid_password(request.POST['secretcode'])
                if error is None:
                    room = form.save(commit=False)
                    room.save()
                    room.users.add(request.user)
                    return HttpResponse("Go to the new created room")
                else:
                    return render(request, 'start/profile.html', context={'form': RoomForm(),
                                                                          'error_password': error})
            else:
                return HttpResponse("form not valid")
        elif request.method == 'POST' and 'join' in request.POST:
            form = JoinForm(request.POST)
            if form.is_valid():
                error = valid_password(request.POST['secretcode'])
                if error is None:
                    temp = Room.objects.filter(name=request.POST['name'], secretcode=request.POST['secretcode']).first()
                    if temp is None:
                        return render(request, 'start/profile.html', context={'form': RoomForm(), 'form1': JoinForm(),
                                                                            'error_group': "Invalid group or password"})
                    else:
                        temp.users.add(request.user)
                        return HttpResponse("Joining the room")
                else:
                    return render(request, 'start/profile.html', context={'form': RoomForm(), 'form1': JoinForm(),
                                                                          'error_group': "Invalid group or password"})
            else:
                return HttpResponse("Your say shit")
        elif request.method == 'POST' and 'logout' in request.POST:
            logout(request)
            return redirect('index')
        elif request.method == 'GET':
            return render(request, 'start/profile.html', context={'form': RoomForm(), 'form1': JoinForm()})
    else:
        return HttpResponse("Lie")



# TODO: Make the logout function