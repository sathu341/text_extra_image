# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Person, Student

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()

    class Meta:
        model =Person
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class StudentForm(forms.ModelForm):
    student_id = forms.CharField(max_length=10)
    grade = forms.CharField(max_length=2)

    class Meta:
        model = Student
        fields = ['student_id', 'grade']
