from django.db import models
from django.core.validators import *
from django.core import validators

class Category(models.Model):
    category_name = models.CharField(max_length=200, null=True, validators=[validators.MinLengthValidator(2)])
    def __str__(self):
        return self.category_name

class News(models.Model):
    news_title = models.CharField(max_length=200)
    news_description_title = models.CharField(max_length=200,null=True)
    news_description = models.TextField(null=True)
    news_image = models.FileField(upload_to='static/uploads')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.news_title

