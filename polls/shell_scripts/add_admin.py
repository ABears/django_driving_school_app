from django.contrib.auth.models import Group, User
from polls.models import UserModel
from polls.models import Package

def add_admin():
    user = UserModel.objects.get(
                email = 'Doe@gmail.com'
            )
    admin_group = Group.objects.get(name='administrator')
    user.groups.add(admin_group)
    print('Administrator created')

add_admin()