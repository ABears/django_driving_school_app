import json
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
# from django.contrib.auth.models import User
from django.shortcuts import redirect
from polls.models import Package
from polls.forms import LoginForm



def index(request):
    all_packages = Package.objects.all()        
    context = {'all_packages': all_packages}
    if request.POST:
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
        
            return redirect('/')

    return render(request, 'home.html', context)

def connection(request):
    all_packages = Package.objects.all()        
    context = {'all_packages': all_packages}

    if request.POST:
        login_form = LoginForm(request.POST) 
        if login_form.is_valid():
            # user.authenticate()
            return redirect('/')

    return render(request, 'connection.html', context)