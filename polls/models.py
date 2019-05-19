import uuid
from django.db import models
from django.contrib.auth.models import User, AbstractUser



# Custom django auth models
class UserModel(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=500, default=None, unique=True)
    first_name = models.CharField(max_length=500, default=None)
    last_name = models.CharField(max_length=500, default=None)
    email = models.CharField(max_length=500, default=None)
    password = models.CharField(max_length=500, default=None)
    is_active = models.BooleanField(default=True)
    forfait_hour = models.IntegerField(default=None)
    images = models.CharField(max_length=500, default=None)


class Package(models.Model):
    id = models.CharField(max_length=100, blank=False, primary_key=True, unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=500, default=None)
    images = models.CharField(max_length=500, default=None)
    forfait_hour = models.IntegerField(blank=False)
    price = models.IntegerField(blank=True, default=999)

class Forfait(models.Model):
    id = models.CharField(max_length=100, blank=False, primary_key=True, unique=True, default=uuid.uuid4)
    hour = models.IntegerField(blank=False)

class Appointement(models.Model):
    id = models.CharField(max_length=100, blank=False, primary_key=True, unique=True, default=uuid.uuid4)
    appointement_date = models.DateTimeField()
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE, default=None)

class Instructor_class(models.Model):
    id = models.CharField(max_length=100, blank=False, primary_key=True, unique=True, default=uuid.uuid4)
    instructor_id = models.ForeignKey(UserModel, blank=False, on_delete=models.CASCADE, related_name='instructor_content_type')
    student_id = models.ForeignKey(UserModel, blank=False, on_delete=models.CASCADE, related_name='student_content_type')