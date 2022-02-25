from django.db import models
from django.contrib.auth.models import User



class Profile_doc(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    profile_pic = models.FileField(upload_to='static/profile', default='static/img/default_user.png')
    created_date = models.DateTimeField(auto_now_add=True)
