from django.db import models

# Create your models here.
# models.py

from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=10)
    grade = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.person.first_name} {self.person.last_name} (Student)"

