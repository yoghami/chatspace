
from django.shortcuts import render, HttpResponse ,HttpResponseRedirect
from django.contrib.auth.password_validation import get_default_password_validators, ValidationError
from django.contrib.auth import authenticate, login

from . forms import userRegestration
# Create your views here.

def index(request):

   return render(request, "index/index.html", context={'form': userRegestration()})

def signup(request):
    if request.method == 'POST':
        form = userRegestration(request.POST)

        if form.is_valid():
            error = valid_password(request.POST['password'])
            print(error)
            if error is None:

                user = form.save(commit=False)

                user.set_password(request.POST['password'])

                user.save()
                return render(request, "index/index.html", context={'form': userRegestration()})
            else:
                return render(request, "index/index.html", context={'form': userRegestration(),
                                                                    'error_passowrd': error})

        else:
            print(form.errors)
            return HttpResponse("fail")




def logIN(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request,username=username,password=password)

    print(user)
    if user is not None:
        login(request, user)

        return HttpResponse("personal page")
    else:
        return render(request, "index/index.html", context={'form': userRegestration(),
                                                            'logerror': 'username or password are not valid'})


# valid password

def valid_password(password, user=None):

    validators = get_default_password_validators()

    for validator in validators:
        try:
            validator.validate(password, user)
        except ValidationError as error:
            print(error.messages[0])
            return error.messages[0]

