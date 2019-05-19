from django.db import models
import uuid

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
    user = models.ForeignKey(Users, blank=False, on_delete=models.CASCADE)

class Appointement(models.Model):
    id = models.CharField(max_length=100, blank=False, primary_key=True, unique=True, default=uuid.uuid4)
    appointement_date = models.DateTimeField()
    user = models.ForeignKey(Users, blank=False, on_delete=models.CASCADE)

class Instructor_class():
    id = models.CharField(max_length=100, blank=False, primary_key=True, unique=True, default=uuid.uuid4)
    instructor_id = role = models.ForeignKey(Users, blank=False, on_delete=models.PROTECT)
    student_id = role = models.ForeignKey(Users, blank=False, on_delete=models.PROTECT)
