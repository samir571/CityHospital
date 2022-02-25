from django import forms
from django.forms import ModelForm

from .models import Category, Doctor

class CategoryForm(ModelForm):
    class Meta:
        model= Category
        fields = "__all__"


class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"
