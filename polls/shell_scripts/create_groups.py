from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.models import User
from polls.models import Appointement

# Group creation
administrator_group, created = Group.objects.get_or_create(name='administrator')
secretary_group, created = Group.objects.get_or_create(name='secretary')
instructor_group, created = Group.objects.get_or_create(name='instructor')
student_group, created = Group.objects.get_or_create(name='student')

# Create content type
user_type = ContentType.objects.get_for_model(User)
appointement_type = ContentType.objects.get_for_model(Appointement)

# Create secretary permissions
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

# Create student permissions
create_student_account = Permission.objects.create(codename='create_student_account',
                                   name='Can create student account', 
                                   content_type=user_type)

read_student_account = Permission.objects.create(codename='read_student_account',
                                   name='Can read student account', 
                                   content_type=user_type)

edit_student_account = Permission.objects.create(codename='edit_student_account',
                                   name='Can edit student account', 
                                   content_type=user_type)

delete_student_account = Permission.objects.create(codename='delete_student_account',
                                   name='Can delete student account', 
                                   content_type=user_type)

# Create instuctor permissions
create_instructor_account = Permission.objects.create(codename='create_instructor_account',
                                   name='Can create instructor account', 
                                   content_type=user_type)

read_instructor_account = Permission.objects.create(codename='read_instructor_account',
                                   name='Can read instructor account', 
                                   content_type=user_type)

edit_instructor_account = Permission.objects.create(codename='edit_instructor_account',
                                   name='Can edit instructor account', 
                                   content_type=user_type)

delete_instructor_account = Permission.objects.create(codename='delete_instructor_account',
                                   name='Can delete instructor account', 
                                   content_type=user_type)

# Create appointement permissions
create_appointement = Permission.objects.create(codename='create_appointement',
                                   name='Can create appointement', 
                                   content_type=appointement_type)

read_appointement = Permission.objects.create(codename='read_appointement',
                                   name='Can read appointement', 
                                   content_type=appointement_type)

edit_appointement = Permission.objects.create(codename='edit_appointement',
                                   name='Can edit appointement', 
                                   content_type=appointement_type)

delete_appointement = Permission.objects.create(codename='delete_appointement',
                                   name='Can delete appointement', 
                                   content_type=appointement_type)
# Create course hour permissions 
create_course_hour = Permission.objects.create(codename='create_course_hour',
                                   name='Can add course hour to student', 
                                   content_type=user_type)

# Create course planning permissions 
read_driving_school_planning = Permission.objects.create(codename='read_driving_school_planning',
                                   name='Can read driving school planning', 
                                   content_type=appointement_type)

# Read course planning permissions 
read_own_student_profil = Permission.objects.create(codename='read_own_student_profil',
                                   name='Read own student profil', 
                                   content_type=user_type)

# Create course planning permissions 
read_own_appointement = Permission.objects.create(codename='read_own_appointement',
                                   name='Can read own appoinement', 
                                   content_type=appointement_type)

# Add secretary crud to admin
administrator_group.permissions.add(create_secretary_account)
administrator_group.permissions.add(read_secretary_account)
administrator_group.permissions.add(edit_secretary_account) 
administrator_group.permissions.add(delete_secretary_account)

# Add instructor crud to admin
administrator_group.permissions.add(create_instructor_account)
administrator_group.permissions.add(read_instructor_account)
administrator_group.permissions.add(edit_instructor_account) 
administrator_group.permissions.add(delete_instructor_account)

# Add student crud to admin
administrator_group.permissions.add(create_student_account)
administrator_group.permissions.add(read_student_account)
administrator_group.permissions.add(edit_student_account) 
administrator_group.permissions.add(delete_student_account)


# Add appointement crud to admin
administrator_group.permissions.add(create_appointement)
administrator_group.permissions.add(read_appointement)
administrator_group.permissions.add(edit_appointement) 
administrator_group.permissions.add(delete_appointement)

# Add reading planning permission to admin
administrator_group.permissions.add(read_driving_school_planning)

# Add create course hour right crud to admin
administrator_group.permissions.add(create_course_hour)

# Add instructor crud to secretary
secretary_group.permissions.add(create_instructor_account)
secretary_group.permissions.add(read_instructor_account)
secretary_group.permissions.add(edit_instructor_account) 
secretary_group.permissions.add(delete_instructor_account)

# Add student crud to secretary
secretary_group.permissions.add(create_student_account)
secretary_group.permissions.add(read_student_account)
secretary_group.permissions.add(edit_student_account) 
secretary_group.permissions.add(delete_student_account)


# Add appointement crud to secretary
secretary_group.permissions.add(create_appointement)
secretary_group.permissions.add(read_appointement)
secretary_group.permissions.add(edit_appointement) 
secretary_group.permissions.add(delete_appointement)

# Add reading planning permission to secretary
secretary_group.permissions.add(read_driving_school_planning)

# Add create course hour right to secretary
secretary_group.permissions.add(create_course_hour)

# Add appointement crud to instructor
instructor_group.permissions.add(create_appointement)
instructor_group.permissions.add(read_appointement)
instructor_group.permissions.add(edit_appointement) 
instructor_group.permissions.add(delete_appointement)

# Add reading own student profil permission to instructor
instructor_group.permissions.add(read_own_student_profil)

# Add appointement create and read own to student
student_group.permissions.add(create_appointement)
student_group.permissions.add(read_own_appointement)
