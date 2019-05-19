from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.models import User
from polls.models import Appointement

administrator_group = Group.objects.get_or_create(name='administrator')
secretary_group = Group.objects.get_or_create(name='secretary')
instructor_group = Group.objects.get_or_create(name='instructor')
student_group = Group.objects.get_or_create(name='student')

user_type = ContentType.objects.get_for_model(User)
appointement_type = ContentType.objects.get_for_model(User)


# Now what - Say I want to add 'Can add project' permission to new_group?
create_secretary_account = Permission.objects.create(codename='create_secretary_account',
                                   name='Can create secretary account', 
                                   content_type=user_type)

read_secretary_account = Permission.objects.create(codename='read_secretary_account',
                                   name='Can read secretary account', 
                                   content_type=user_type)

edit_secretary_account = Permission.objects.create(codename='edit_secretary_account',
                                   name='Can edit secretary account', 
                                   content_type=user_type)

delete_secretary_account = Permission.objects.create(codename='delete_secretary_account',
                                   name='Can delete secretary account', 
                                   content_type=user_type)

# Add secretary crud to admin
administrator_group.permissions.add(create_secretary_account)
administrator_group.permissions.add(read_secretary_account)
administrator_group.permissions.add(delete_secretary_account)
administrator_group.permissions.add(permission_2) 