import json
import uuid
from django.contrib import messages
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
from polls.forms import LoginForm, RegisterForm, UpdateForm
    
def admin_panel(request):

    is_secratery = request.user.groups.filter(name='secretary').exists()
    is_administrator  = request.user.groups.filter(name='administrator').exists()
    get_administrators = UserModel.objects.filter(groups__name="administrator", is_active=True)
    get_secretary = UserModel.objects.filter(groups__name="secretary", is_active=True)
    get_instructors = UserModel.objects.filter(groups__name="instructor", is_active=True)
    get_students = UserModel.objects.filter(groups__name="student", is_active=True)

    if is_administrator or is_administrator:
        context = {
            'administrators': get_administrators,
            'secretarys': get_secretary,
            'instructors': get_instructors,
            'students': get_students
        }
    else:
        redirect('/')

    return render(request, 'admin-panel/admin-panel.html', context)

# USER CRUD
def create_user(request):

    is_secratery = request.user.groups.filter(name='secretary').exists()
    is_administrator  = request.user.groups.filter(name='administrator').exists()

    if is_administrator or is_secratery:
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
                return redirect('/admin-panel')

    else:
        redirect('/')

    context = {
        'form': register_form,
        'subject': 'user',
        'description': 'Add user to hour driving school and let him get all the famous advantage and lessons of our Driving School.'
    }
    
    return render(request, 'admin-panel/add-user.html', context)
    

def read_student(request, id):

    is_secratery = request.user.groups.filter(name='secretary').exists()
    is_administrator  = request.user.groups.filter(name='administrator').exists()
    get_instructors = UserModel.objects.filter(groups__name="instructor", is_active=True)
    get_students = UserModel.objects.filter(groups__name="student", is_active=True)

    if is_administrator or is_secratery:
        try:    
            get_user = UserModel.objects.get(id=id)
        except:
            messages.success(request, 'User not found')      
    else:
        redirect('/')

    context = {
        'subject_user': get_user,
        'students': get_students,
        'instructors': get_instructors
    }
    
    return render(request, 'admin-panel/single-user.html', context)     

def update_student(request, id):

    is_administrator  = request.user.groups.filter(name='administrator').exists()
    is_secratery  = request.user.groups.filter(name='administrator').exists()
    update_form = None
    
    try:
        get_user = UserModel.objects.get(id=id)
    except:
        messages.success(request, 'User not found')
        return redirect('/admin-panel')

    if is_administrator or is_secratery:

        if request.POST:
            update_form = UpdateForm(request.POST)
            # Registration form
            if update_form.is_valid():
                data = request.POST.copy()    
                get_user.first_name = data.get('first_name')
                get_user.last_name = data.get('last_name')
                get_user.email = data.get('email') 
                get_user.save()
                messages.success(request, 'This user as been successfully updated')
                return redirect('/admin-panel')
                             
    else:
        redirect('/')

    context = {
        'form': update_form,
        'subject_user': get_user,
        'subject': 'secretary',
        'description': ''
    }
    
    return render(request, 'admin-panel/update-user.html', context)

def delete_student(request, id):

    is_secratery = request.user.groups.filter(name='secretary').exists()
    is_administrator  = request.user.groups.filter(name='administrator').exists()

    if is_administrator or is_secratery:

        try:    
            get_user = UserModel.objects.get(id=id)
            if get_user:
                get_user.is_active = False 
                get_user.save()
                messages.success(request, 'This user as been successfully deleted')
        except:
            messages.success(request, 'User not found')

    else:
        redirect('/')

    return redirect('/admin-panel')

# INSTRUCTOR CRUD
def create_instructor(request):
    
    is_secratery = request.user.groups.filter(name='secretary').exists()
    is_administrator  = request.user.groups.filter(name='administrator').exists()

    if is_administrator or is_secratery:
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
                student_group = Group.objects.get(name='instructor')
                    
                user.groups.add(student_group)
                return redirect('/admin-panel')

    else:
        redirect('/')

    context = {
        'form': register_form,
        'subject': 'instructor',
        'description': ''
    }
    
    return render(request, 'admin-panel/add-user.html', context)

def read_instructor(request, id):

    is_secratery = request.user.groups.filter(name='secretary').exists()
    is_administrator  = request.user.groups.filter(name='administrator').exists()
    get_instructors = UserModel.objects.filter(groups__name="instructor", is_active=True)
    get_students = UserModel.objects.filter(groups__name="student", is_active=True)

    if is_administrator or is_secratery:
        try:    
            get_user = UserModel.objects.get(id=id)
        except:
            messages.success(request, 'User not found')      
    else:
        redirect('/')

    context = {
        'subject_user': get_user,
        'students': get_students,
        'instructors': get_instructors
    }
    
    return render(request, 'admin-panel/single-user.html', context)  


def update_instructor(request, id):

    is_secratery = request.user.groups.filter(name='secretary').exists()
    is_administrator  = request.user.groups.filter(name='administrator').exists()
    update_form = None
    
    try:
        get_user = UserModel.objects.get(id=id)
    except:
        messages.success(request, 'User not found')
        return redirect('/admin-panel')

    if is_administrator or is_secratery:

        if request.POST:
            update_form = UpdateForm(request.POST)
            # Registration form
            if update_form.is_valid():
                data = request.POST.copy()    
                get_user.first_name = data.get('first_name')
                get_user.last_name = data.get('last_name')
                get_user.email = data.get('email') 
                get_user.save()
                messages.success(request, 'This user as been successfully updated')
                return redirect('/admin-panel')
    else:
        redirect('/')

    context = {
        'form': update_form,
        'subject': 'secretary',
        'subject_user': get_user,
        'description': ''
    }
    
    return render(request, 'admin-panel/update-user.html', context)

def delete_instructor(request, id):

    is_secratery = request.user.groups.filter(name='secretary').exists()
    is_administrator  = request.user.groups.filter(name='administrator').exists()

    if is_administrator or is_secratery:

        try:    
            get_user = UserModel.objects.get(id=id)
            if get_user:
                get_user.is_active = False 
                get_user.save()
                messages.success(request, 'This user as been successfully deleted')
        except:
            messages.success(request, 'User not found')

    else:
        redirect('/')


    return redirect('/admin-panel')

# SECRETARY CRUD
def create_secretary(request):

    is_administrator  = request.user.groups.filter(name='administrator').exists()

    if is_administrator:
        update_form = None

        if request.POST:
            update_form = RegisterForm(request.POST)
            # Registration form
            if update_form.is_valid():
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
                student_group = Group.objects.get(name='secretary')
                    
                user.groups.add(student_group)
                return redirect('/admin-panel')

    else:
        redirect('/')

    context = {
        'form': update_form,
        'subject': 'secretary',
        'description': ''
    }
    
    return render(request, 'admin-panel/add-user.html', context)

def read_secretary(request, id):

    is_administrator  = request.user.groups.filter(name='administrator').exists()

    if is_administrator or is_secratery:
        try:    
            get_user = UserModel.objects.get(id=id)
        except:
            messages.success(request, 'User not found')     
    else:
        redirect('/')

    context ={
        'subject_user': get_user
    }

    return render(request, 'admin-panel/single-user.html', context)    

def update_secretary(request, id):

    is_administrator  = request.user.groups.filter(name='administrator').exists()
    update_form = None
    
    try:
        get_user = UserModel.objects.get(id=id)
    except:
        messages.success(request, 'User not found')
        return redirect('/admin-panel')

    if is_administrator:

        if request.POST:
            update_form = RegisterForm(request.POST)
            # Registration form
            if update_form.is_valid():
                data = request.POST.copy()    
                get_user.first_name = data.get('first_name')
                get_user.last_name = data.get('last_name')
                get_user.email = data.get('email') 
                get_user.save()
                messages.success(request, 'This user as been successfully updated')
                return redirect('/admin-panel')

    else:
        redirect('/')

    context = {
        'form': update_form,
        'subject': 'secretary',
        'subject_user': get_user,
        'description': ''
    }
    
    return render(request, 'admin-panel/update-user.html', context)


def delete_secretary(request, id):

    is_secratery = request.user.groups.filter(name='secretary').exists()
    is_administrator  = request.user.groups.filter(name='administrator').exists()

    if is_administrator or is_secratery:

        try:    
            get_user = UserModel.objects.get(id=id)
            if get_user:
                get_user.is_active = False 
                get_user.save()
                messages.success(request, 'This user as been successfully deleted')
        except:
            messages.success(request, 'User not found')

    else:
        redirect('/')

    return redirect('/admin-panel')


