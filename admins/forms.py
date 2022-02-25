from django import forms

from django import forms
from django.forms import ModelForm
from .models import Notice


class NoticeForm(ModelForm):
    class Meta:
        model = Notice
        fields = "__all__"