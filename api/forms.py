from django import forms
from .models import *

def check_age(value):
    if value < 2: 
        raise forms.ValidationError("age must be grater than 1")

def check_name(value):
    if not value:
        raise forms.ValidationError("first name can't be empty")
    if value[0].islower():
        raise forms.ValidationError("first char in first name must be capital")

class StudentForm(forms.ModelForm):
    age = forms.IntegerField(validators=[check_age])
    first_name = forms.CharField(max_length=256, validators=[check_name])
    last_name = forms.CharField(max_length=256, validators=[check_name])
    class Meta:
        model = Student
        fields = "__all__"
