import json
import uuid
from django.contrib.auth import logout
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django import template
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import Group, User
from polls.models import UserModel
from polls.models import Package
from polls.forms import LoginForm, RegisterForm

register = template.Library()

@register.filter(name='has_group') 
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists() 
    
def index(request):

    # Package offers
    all_packages = Package.objects.all()  
    register_form = None

    if request.POST:
        register_form = RegisterForm(request.POST)
        # Registration form
        if register_form.is_valid():
            data = request.POST.copy()
            user = UserModel.objects.create_user(
                                    username = uuid.uuid4(),
                                    password = data.get('password'),
                                    email = data.get('email'),
                                    first_name = data.get('first_name'),
                                    last_name = data.get('last_name'),
                                    forfait_hour = 20,
                                    images= "default.jpg"
                                )
            student_group = Group.objects.get(name='student')
            user.groups.add(student_group)
            return redirect('/login')

    context = {
        'all_packages': all_packages,
        'form': register_form
    }

    return render(request, 'home.html', context)

def connection(request):
    login_form = None

    if request.POST:
        login_form = LoginForm(request.POST) 
        if login_form.is_valid():

            data = request.POST.copy()
            
            try:
                user = UserModel.objects.get(email=data.get('email'), is_active=True)
                is_check_password = user.check_password(data.get('password'))
            except:
                return redirect('/login')

            if user and is_check_password:
                login(request, user)
                return redirect('/')

    context = {'form': login_form}

    return render(request, 'login.html', context)

def disconnection(request):
    logout(request)
    return redirect('/')