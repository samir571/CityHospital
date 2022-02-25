from django.db import models
from doctor.models import Category
from django import forms
from django.contrib.auth.models import User



class Appointment(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    date = models.CharField(max_length=200)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    number = models.CharField(max_length=200)
    message = models.TextField(null=True)

    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name



class Contact_Us(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField(null=True)
    def __str__(self):
        return self.full_name

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    profile_pic = models.FileField(upload_to='static/profile', default='static/img/default_user.png')
    created_date = models.DateTimeField(auto_now_add=True)


class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answers = models.TextField(null=True)

    def __str__(self):
        return self.question
