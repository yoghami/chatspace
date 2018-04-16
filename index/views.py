
from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, "index/index.html", context={})

