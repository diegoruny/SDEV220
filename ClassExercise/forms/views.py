from django.shortcuts import render
from .models import UserInfo

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserInfo(request.POST)
        if form.is_valid():
            form.save()

    return render(request, "static/registration.html")

def login(request):
    return render(request, "static/login.html")