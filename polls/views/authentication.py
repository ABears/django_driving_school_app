import json
import uuid
import hashlib
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import Group, User
from polls.models import UserModel
from polls.models import Package
from polls.forms import LoginForm, RegisterForm



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
                                    forfait_hour = 0,
                                    images= "default.jpg"
                                )
            student_group = Group.objects.get(name='student')
            user.groups.add(student_group)
            return redirect('/connection')

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
            user = UserModel.objects.get(email=data.get('email'))
            is_check_password = user.check_password(data.get('password'))

            if user and is_check_password:
                login(request, user)
                return redirect('/')

    context = {'form': login_form}

    return render(request, 'connection.html', context)