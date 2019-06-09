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

# APPOINTEMENT CRUD
def create_appointement(request, id, student_id, instructor_id):

    instructor = UserModel.objects.get(id=instructor_id)
    student = UserModel.objects.get(id=student_id)
    
    instructor_student = instructor.get_students.get(id=student_id)


    if request.method == 'POST' and instructor_student:

        get_appointement = request.POST.get('appointement')
        format_appointement = datetime.datetime.strptime(get_appointement, '%d/%m/%Y %H:%M:%S')

        appointement_exist = Appointement.objects.filter(appointement_date=format_appointement, instructor_id=instructor_id).all()

        if len(appointement_exist) == 0:
                        
            appointement = Appointement.objects.create(
                        appointement_date = format_appointement,
                        student = student,
                        instructor = instructor
                    )

            return JsonResponse({
                'success': 'This date is now registered',
                'appointement': appointement.appointement_date,
            })
        
        return JsonResponse({
            'error': "This appointement is all ready used"
        })


    else:
        return redirect('/')

    
def read_appointement(request, user_id):

    get_user = UserModel.objects.get(id=user_id)

    user_is_student = get_user.groups.filter(name='student').exists()
    user_is_instructor = get_user.groups.filter(name='instructor').exists()

    if user_is_student:
        appointement = Appointement.objects.filter(student=user_id).values()
    elif user_is_instructor:
        appointement = Appointement.objects.filter(instructor_id=user_id).values()
    else:
        return JsonResponse({
            'error': 'Can\'t access to this calendar'
        })
    
    return JsonResponse({
        'all_appointement': list(appointement)
    })

    context = {
        'form': register_form,
        'subject': 'user',
        'description': 'Add user to hour driving school and let him get all the famous advantage and lessons of our Driving School.'
    }
    
    return render(request, 'admin-panel/add-user.html', context)


# READ DAY PLANNING
def read_day_planning(request, user_id, subject_date):

    get_user = UserModel.objects.get(id=user_id)

    user_is_student = get_user.groups.filter(name='student').exists()
    user_is_instructor = get_user.groups.filter(name='instructor').exists()

    parsing_date = datetime.datetime.strptime(subject_date, '%d-%m-%Y')

    if user_is_student:
        appointement = Appointement.objects.filter(student=user_id, appointement_date__startswith=datetime.date(int(parsing_date.year), int(parsing_date.month), int(parsing_date.day))).values()
    elif user_is_instructor:
        appointement = Appointement.objects.filter(instructor_id=user_id, appointement_date__startswith=datetime.date(int(parsing_date.year) ,int(parsing_date.month),int(parsing_date.day))).values()
    else:
        return JsonResponse({
            'error': 'Can\'t access to this calendar'
        })
    
    return JsonResponse({
        'all_appointement': list(appointement)
    })

    context = {
        'form': register_form,
    }
    
    return render(request, 'admin-panel/add-user.html', context)


def delete_appointement(request, user_id, appointement_id):

    is_secratery = request.user.groups.filter(name='secretary').exists()
    is_administrator = request.user.groups.filter(name='administrator').exists()
    is_instructor = request.user.groups.filter(name='instructor').exists()
    is_student = request.user.groups.filter(name='student').exists()

    get_user = UserModel.objects.get(id=user_id)

    user_is_student = get_user.groups.filter(name='student').exists()
    user_is_instructor = get_user.groups.filter(name='instructor').exists()

    if user_is_student:
        appointement = Appointement.objects.get(student_id=user_id, id=appointement_id)
    elif user_is_instructor:
        appointement = Appointement.objects.get(instructor_id=user_id, id=appointement_id)

    if request.method == 'POST':

        if is_secratery or is_administrator:
            appointement = Appointement.objects.get(id=appointement_id)
            appointement.delete()
        elif user_is_instructor or user_is_student:
            appointement.delete()

    else:
        redirect('/')

    return JsonResponse({
        'success': 'Your appointement has been deleted'
    })

