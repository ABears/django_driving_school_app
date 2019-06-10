import json
import uuid
import pdb
import datetime
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django import template
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import Group, User
from polls.models import UserModel, Appointement
from polls.models import Package
from polls.forms import LoginForm, RegisterForm, UpdateForm

def admin_panel(request):

    is_secratery = request.user.groups.filter(name='secretary').exists()
    is_administrator  = request.user.groups.filter(name='administrator').exists()
    get_administrators = UserModel.objects.filter(groups__name="administrator", is_active=True)
    get_secretary = UserModel.objects.filter(groups__name="secretary", is_active=True)
    get_instructors = UserModel.objects.filter(groups__name="instructor", is_active=True)
    get_students = UserModel.objects.filter(groups__name="student", is_active=True)

    if is_administrator or is_secratery:
        context = {
            'administrators': get_administrators,
            'secretarys': get_secretary,
            'instructors': get_instructors,
            'students': get_students
        }
    else:
        redirect('/')

    return render(request, 'admin-panel/admin-panel.html', context)

def read_driving_school_planning(request):
    return render(request, 'admin-panel/calendar.html')

def read_all_planning(request):

    appointement = Appointement.objects.values()

    return JsonResponse({
        'all_appointement': list(appointement)
    })

def read_day_general_planning(request, subject_date):

    parsing_date = datetime.datetime.strptime(subject_date, '%d-%m-%Y')
    appointement = Appointement.objects.filter(appointement_date__startswith=datetime.date(int(parsing_date.year), int(parsing_date.month), int(parsing_date.day))).order_by('-appointement_date').reverse().values()
    
    return JsonResponse({
        'all_appointement': list(appointement)
    })

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
                                        forfait_hour = 20,
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
    is_student = request.user.groups.filter(name='student').exists()

    get_instructors = UserModel.objects.filter(groups__name="instructor", is_active=True)
    get_students = UserModel.objects.filter(groups__name="student", is_active=True)
    student_instructor = ''

    if is_student: 
        try:    
            get_user = UserModel.objects.get(id=id)
            if get_user.id != request.user.id:
                return redirect('/')
            else:
                is_owner = True
        except:
            return redirect('/')

    for instructor in get_instructors:
        get_student = instructor.get_students.filter(id=id)
        if len(get_student) > 0:
            student_instructor = instructor


    if is_administrator or is_secratery or is_owner:
        try:    
            get_user = UserModel.objects.get(id=id)
        except:
            messages.success(request, 'User not found')     
            
    else:
        redirect('/')

    context = {
        'subject_user': get_user,
        'students': get_students,
        'instructors': student_instructor
    }
    
    return render(request, 'admin-panel/single-user.html', context)     

def update_student(request, id):

    is_administrator  = request.user.groups.filter(name='administrator').exists()
    is_secratery  = request.user.groups.filter(name='secretary').exists()
    update_form = None
    
    try:
        get_user = UserModel.objects.get(id=id)
    except:
        messages.success(request, 'User not found')
        return redirect('/admin-panel')

    if is_administrator or is_secratery:
        get_user = UserModel.objects.get(id=id)
        if request.POST:
            update_form = UpdateForm(request.POST, get_user=get_user)
            # Registration form
            
            if update_form.is_valid():
                data = request.POST.copy()    
                get_user.first_name = data.get('first_name')
                get_user.last_name = data.get('last_name')
                get_user.email = data.get('email') 
                get_user.forfait_hour = data.get('forfait_hour') 
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

    if is_administrator or is_secratery:
        try:    
            get_user = UserModel.objects.get(id=id)
            get_students = get_user.get_students.all()
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
            update_form = UpdateForm(request.POST, get_user=get_user)
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
            update_form = UpdateForm(request.POST, get_user=get_user)
            
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


def attribute_student(request, instructor_id, student_id):
    
    get_instructor = UserModel.objects.get(id=instructor_id)
    get_student = UserModel.objects.get(id=student_id)

    # instructor_is_instructor = get_instructor.groups.filter(groups__name='instructor').exists()
    # student_is_student = get_student.groups.filter(groups__name='student').exists()

    get_instructor_group = Group.objects.get(user = get_instructor)
    get_student_group = Group.objects.get(user = get_student)

    if get_instructor_group.name == 'instructor' and get_student_group.name == 'student':
        
        get_instructor.get_students.add(get_student)

        return JsonResponse({
            'success':  'Student as been added to class'
        })

    return JsonResponse({
        'error': 'Something is went wrong please try again later'
    })
    
def not_attribute_student(request):

    is_secratery = request.user.groups.filter(name='secretary').exists()
    is_administrator  = request.user.groups.filter(name='administrator').exists()

    get_instructors = UserModel.objects.filter(groups__name="instructor", is_active=True).values()
    get_attribute_student = []

    for instructor in get_instructors:
        current_instructor = UserModel.objects.get(id=instructor['id'])
        all_instructor_student = current_instructor.get_students.all()
        
        for instructor_student in all_instructor_student:
            get_attribute_student.append(instructor_student.id)

    not_attributed_users = UserModel.objects.filter(groups__name="student", is_active=True).exclude(id__in=get_attribute_student)

    if is_administrator or is_secratery:
        context = {
        'students': not_attributed_users,
        'instructors': get_instructors
        }
    else:
        redirect('/')

    return render(request, 'admin-panel/non-attribute-student.html', context)


def read_user(request, id):

    get_user = UserModel.objects.filter(id=id).values()

    return JsonResponse({
        'subject_user': list(get_user)
    })