import json
import uuid
from django import template
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.models import Group, User
from polls.models import UserModel
from polls.models import Package

# USER CRUD
def create_appointement(request, id, student_id, instructor_id):

    is_secratery = request.user.groups.filter(name='secretary').exists()
    is_administrator = request.user.groups.filter(name='administrator').exists()
    is_instructor = request.user.groups.filter(name='instructor').exists()
    is_student = request.user.groups.filter(name='student').exists()

    if request.method == 'POST':

        return JsonResponse({
            'jsonresponse': 'jsonresponse'
        })

    else:
        redirect('/')

    context = {
        'form': register_form,
        'subject': 'user',
        'description': 'Add user to hour driving school and let him get all the famous advantage and lessons of our Driving School.'
    }
    
    return render(request, 'admin-panel/add-user.html', context)


# USER CRUD
def read_appointement(request, id, student_id, instructor_id):

    is_secratery = request.user.groups.filter(name='secretary').exists()
    is_administrator = request.user.groups.filter(name='administrator').exists()
    is_instructor = request.user.groups.filter(name='instructor').exists()
    is_student = request.user.groups.filter(name='student').exists()

    if request.method == 'POST':

        return JsonResponse({
            'json_response': 'json_response'
        })

    else:
        redirect('/')

    context = {
        'form': register_form,
        'subject': 'user',
        'description': 'Add user to hour driving school and let him get all the famous advantage and lessons of our Driving School.'
    }
    
    return render(request, 'admin-panel/add-user.html', context)


# USER CRUD
def update_appointement(request, id, appointement_id):

    is_secratery = request.user.groups.filter(name='secretary').exists()
    is_administrator = request.user.groups.filter(name='administrator').exists()
    is_instructor = request.user.groups.filter(name='instructor').exists()
    is_student = request.user.groups.filter(name='student').exists()

    if request.method == 'POST':

        return JsonResponse({
            'json_response': 'json_response'
        })

    else:
        redirect('/')

    context = {
        'form': register_form,
        'subject': 'user',
        'description': 'Add user to hour driving school and let him get all the famous advantage and lessons of our Driving School.'
    }
    
    return render(request, 'admin-panel/add-user.html', context)


# USER CRUD
def delete_appointement(request, id, appointement_id):

    is_secratery = request.user.groups.filter(name='secretary').exists()
    is_administrator = request.user.groups.filter(name='administrator').exists()
    is_instructor = request.user.groups.filter(name='instructor').exists()
    is_student = request.user.groups.filter(name='student').exists()

    if request.method == 'POST':

        return JsonResponse({
            'json_response': 'json_response'
        })

    else:
        redirect('/')

    context = {
        'form': register_form,
        'subject': 'user',
        'description': 'Add user to hour driving school and let him get all the famous advantage and lessons of our Driving School.'
    }
    
    return render(request, 'admin-panel/add-user.html', context)
    

