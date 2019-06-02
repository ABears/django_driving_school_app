"""python_my_driving_school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from polls.views import authentication
from polls.views import administration
from polls.views import appointement
from django.urls import path

urlpatterns = [
    path('', authentication.index, name="index"),
    path('login', authentication.connection, name="login"),
    path('logout', authentication.disconnection, name="logout"),
    path('admin-panel', administration.admin_panel, name="admin-panel"),
    path('create-user', administration.create_user, name="create-user"),
    path('create-instructor', administration.create_instructor, name="create-instructor"),
    path('create-secretary', administration.create_secretary, name="create-secretary"),
    path('read-student/<id>', administration.read_student, name="read-student"),
    path('read-instructor/<id>', administration.read_instructor, name="read-instructor"),
    path('read-secretary/<id>', administration.read_secretary, name="read-secretary"),
    path('update-student/<id>', administration.update_student, name="update-student"),
    path('update-instructor/<id>', administration.update_instructor, name="update-instructor"),
    path('update-secretary/<id>', administration.update_secretary, name="update-secretary"),
    path('delete-student/<id>', administration.delete_student, name="delete-student"),
    path('delete-instructor/<id>', administration.delete_instructor, name="delete-instructor"),
    path('delete-secretary/<id>', administration.delete_secretary, name="delete-secretary"),
    path('create-appointement/<id>/<student_id>/<instructor_id>', appointement.create_appointement, name="create-appointement"),
    path('read-appointement', appointement.read_appointement, name="read-appointement"),
    path('update-appointement', appointement.update_appointement, name="update-appointement"),
    path('delete-appointement', appointement.delete_appointement, name="delete-appointement"),
]
