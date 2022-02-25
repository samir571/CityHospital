from django import forms
from django.forms import ModelForm
from .models import Contact_Us, Appointment, Profile,FAQ

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"
        exclude = ['user']

class ContactForm(ModelForm):
    class Meta:
        model = Contact_Us
        fields = "__all__"

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ['user', 'username']

class FAQForm(ModelForm):
    class Meta:
        model = FAQ
        fields = "__all__"
