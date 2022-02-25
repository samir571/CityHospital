from django.db import models
from django.core.validators import *
from django.core import validators

class Category(models.Model):
    category_name = models.CharField(max_length=200, null=True, validators=[validators.MinLengthValidator(2)])

    def __str__(self):
        return self.category_name


class Doctor(models.Model):
    doctor_name = models.CharField(max_length=200)
    doctor_facebook_link = models.CharField(max_length=200,null=True)
    doctor_instagram_link = models.CharField(max_length=200, null=True)
    doctor_linkedin_link = models.CharField(max_length=200, null=True)
    doctor_twitter_link = models.CharField(max_length=200, null=True)

    doctor_image = models.FileField(upload_to='static/uploads')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.doctor_name


# class Appointment(models.Model):
#     full_name = models.CharField(max_length=200)
#     email = models.CharField(max_length=200)
#     address = models.CharField(max_length=200)
#     age = models.CharField(max_length=200)
#     gender = models.CharField(max_length=200)
#
#     doctor_facebook_link = models.CharField(max_length=200,null=True)
#     doctor_instagram_link = models.CharField(max_length=200, null=True)
#     doctor_linkedin_link = models.CharField(max_length=200, null=True)
#     doctor_twitter_link = models.CharField(max_length=200, null=True)
#
#     doctor_image = models.FileField(upload_to='static/uploads')
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
#     created_date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.doctor_name
#
# class Contact(models.Model):
#     doctor_name = models.CharField(max_length=200)
#     doctor_facebook_link = models.CharField(max_length=200,null=True)
#     doctor_instagram_link = models.CharField(max_length=200, null=True)
#     doctor_linkedin_link = models.CharField(max_length=200, null=True)
#     doctor_twitter_link = models.CharField(max_length=200, null=True)
#
#     doctor_image = models.FileField(upload_to='static/uploads')
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
#     created_date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.doctor_name