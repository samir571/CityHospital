import os

from django.shortcuts import render, redirect
from accounts.auth import unauthenticated_user,admin_only,user_only,doctor_only
from news.models import Category, News
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from accounts.forms import LoginForm, ContactForm, AppointmentForm, ProfileForm
from accounts.auth import unauthenticated_user,admin_only,user_only,doctor_only
from django.contrib.auth.decorators import login_required
from news .models import News
from doctor .models import Doctor
from .models import Profile_doc
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .forms import Profile_doc_Form
from accounts.models import Appointment
from admins.models import Notice
from admins.forms import NoticeForm


@login_required
@doctor_only
def dashboard(request):
    news = News.objects.all().order_by('-id')[:3]
    context = {
        'news': news,
        'activate_news_user': 'active',
    }
    return render(request,'doc/dashboard.html',context)

@login_required
@doctor_only
def show_news(request):
    news = News.objects.all().order_by('-id')
    context={
        'news':news,
        'activate_news_user':'active'

    }
    return render(request, 'doc/show_news.html', context)


@login_required
@doctor_only
def show_notice(request):
    notice = Notice.objects.all().order_by('-id')
    context = {
        'notice': notice,
    }
    return render(request, 'doc/show_notice.html', context)


@login_required
@doctor_only
def show_categories(request):
    categories = Category.objects.all().order_by('-id')
    context={
        'categories':categories,
        'activate_category_user': 'active'

    }
    return render(request, 'doc/show_categories.html', context)



@login_required
@doctor_only
def profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = Profile_doc_Form(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Profile updated successfully")
            return redirect('/doc/profile')
    context = {
        'form': Profile_doc_Form(instance=profile),

    }
    return render(request, 'doc/profile.html', context)


@login_required
@doctor_only
def update_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = Profile_doc_Form(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Profile updated successfully")
            return redirect('/doc/update_profile')
    context = {
        'form': Profile_doc_Form(instance=profile),

    }
    return render(request, 'doc/update_doc_details.html', context)



@login_required
@doctor_only
def change_doc_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.add_message(request, messages.SUCCESS, "Password changed successfully")
            return redirect('/doc/profile')
        else:
            messages.add_message(request, messages.ERROR, "Please verify the form fields")
            return render(request, 'doc/doc_change_password.html' ,{'doc_password_change_form':form})
    context = {
        'doc_password_change_form': PasswordChangeForm(request.user),

    }
    return render(request, 'doc/doc_change_password.html', context)


@login_required
@doctor_only
def my_appointments(request):
    user = request.user
    print(user)
    appointments = Appointment.objects.order_by('-id')
    context = {
        'appointments':appointments,
    }
    return render(request, 'doc/my_appointments.html', context)
