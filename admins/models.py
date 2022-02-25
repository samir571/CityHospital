from django.db import models

from django.db import models
from django.core.validators import *
from django.core import validators


class Notice(models.Model):
    notice_title = models.CharField(max_length=200)
    notice_description = models.TextField()
    notice_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.notice_title
