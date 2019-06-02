import json
import uuid
import datetime
from django import template
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.models import Group, User
from polls.models import UserModel, Appointement
from polls.models import Package

# USER CRUD
def create_appointement(request, id, student_id, instructor_id):

    instructor = UserModel.objects.get(id=instructor_id)
    student = UserModel.objects.get(id=student_id)
    
    instructor_student = instructor.get_students.get(id=student_id)


    if request.method == 'POST' and instructor_student:

        get_appointement = request.POST.get('appointement')
        format_appointement = datetime.datetime.strptime(get_appointement, '%d/%m/%Y %H:%M:%S')

        appointement = Appointement.objects.create(
                            appointement_date = format_appointement,
                            student = student,
                            instructor = instructor
                        )

        appointement.instructor = instructor
        appointement.student = student
        appointement.save()

        return JsonResponse({
            'appointement': appointement.appointement_date,
            'student': instructor_student.first_name
        })

    else:
        return redirect('/')

    
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
    

