from django import forms
from django.forms import ModelForm
from .models import Profile_doc




class Profile_doc_Form(ModelForm):
    class Meta:
        model = Profile_doc
        fields = "__all__"
        exclude = ['user', 'username']