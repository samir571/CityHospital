import os

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, ContactForm, AppointmentForm, ProfileForm, FAQForm
from accounts.auth import unauthenticated_user,admin_only,user_only,doctor_only
from django.contrib.auth.decorators import login_required
from news .models import News
from doctor .models import Doctor
from .models import Contact_Us,Profile,Appointment,FAQ
from django.contrib.auth import update_session_auth_hash


def homepage(request):
    return render(request, 'accounts/index.html')

def doctor(request):
    return render(request,'accounts/doctor.html')

def news(request):
    return render(request,'accounts/news.html')

@unauthenticated_user
def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                if user.is_superuser:
                    login(request,user)
                    return redirect('/admins/dashboard')
                elif user.is_staff:
                    login(request,user)
                    return redirect('/doc/dashboard')
                elif not user.is_staff:
                    login(request, user)
                    return redirect('/')
            else:
                messages.add_message(request,messages.ERROR, "Invalid User cerdentials")
                return render(request,'accounts/login.html',{'form_login':form})
    context={
        'form_login':LoginForm,
        'activate_login': 'active'
    }
    return render(request, 'accounts/login.html',context)

@unauthenticated_user
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Profile.objects.create(user=user, username=user.username, email=user.email)


            messages.add_message(request, messages.SUCCESS, 'User registered successfully')
            return redirect('/login')
        else:
            messages.add_message(request, messages.ERROR, 'unable to register user')
            return render(request,'accounts/register.html',{'form_register':form})
    context = {
        'form_register': UserCreationForm,
        'activate_register': 'active'
    }
    return render(request,'accounts/register.html',context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('/login')

def home_news(request):
    news = News.objects.all().order_by('-id')[:3]
    doctor = Doctor.objects.all().order_by('-id')[:4]
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'appointment requested successfully')
            return redirect("/doctor/get_doctor_user")
        else:
            messages.add_message(request, messages.ERROR,'Unable to request appointment')
            return render(request, 'doctor/show_doctor.html',{'appointment_form':form})
    context={
        'appointment_form' : AppointmentForm,
        'activate_appointment':'active',

        'news':news,
        'activate_news_user':'active',

        'doctor': doctor,
        'activate_doctor_user': 'active',
    }

    return render(request, 'accounts/index.html', context)

def contact_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'message sent successfully')
            return redirect("/contact")
        else:
            messages.add_message(request, messages.ERROR,'Unable to add contact')
            return render(request, 'accounts/contact.html',{'contact_form':form})
    context={
        'contact_form' : ContactForm,
        'activate_contact':'active'
    }

    return render(request, 'accounts/contact.html', context)




# Admin gets the message
@login_required
@admin_only
def get_contact(request):
    contact = Contact_Us.objects.all().order_by('-id')
    context={
        'contact': contact,
        'activate_contact' :'active'
    }
    return render(request, 'accounts/view_contact.html',context)

@login_required
@admin_only
def delete_contact(request, contact_id):
    contact=Contact_Us.objects.get(id=contact_id)
    contact.delete()
    messages.add_message(request, messages.SUCCESS,'message deleted Successfully')
    return redirect('/view_contact')





@login_required
@admin_only
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.add_message(request, messages.SUCCESS, "Password changed successfully")
            return redirect('/change_password')
        else:
            messages.add_message(request, messages.ERROR, "Please verify the form fields")
            return render(request, 'accounts/change_password.html' ,{'password_change_form':form})
    context = {
        'password_change_form': PasswordChangeForm(request.user),

    }
    return render(request, 'accounts/change_password.html', context)

@login_required
@user_only
def profile(request):
    try:
        profile = request.user.profile
    except:
        profile = Profile(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Profile updated successfully")
            return redirect('/profile')
    context = {
        'form': ProfileForm(instance=profile),

    }
    return render(request, 'accounts/profile.html', context)

@login_required
@user_only
def update_profile(request):
    try:
        profile = request.user.profile
    except:
        profile = Profile(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Profile updated successfully")
            return redirect('/update_profile')
    context = {
        'form': ProfileForm(instance=profile),

    }
    return render(request, 'accounts/update_user_details.html', context)



@login_required
@user_only
def change_user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.add_message(request, messages.SUCCESS, "Password changed successfully")
            return redirect('/profile')
        else:
            messages.add_message(request, messages.ERROR, "Please verify the form fields")
            return render(request, 'accounts/user_change_password.html' ,{'user_password_change_form':form})
    context = {
        'user_password_change_form': PasswordChangeForm(request.user),

    }
    return render(request, 'accounts/user_change_password.html', context)





@login_required
@user_only
def my_appointments(request):
    user = request.user
    print(user)
    appointments = Appointment.objects.filter(user=user).order_by('-id')
    context = {
        'appointments':appointments,
    }
    return render(request, 'accounts/my_appointments.html', context)


@login_required
@user_only
def delete_my_appointments(request, apt_id):
    appointments = Appointment.objects.get(id=apt_id)
    appointments.delete()
    messages.add_message(request, messages.SUCCESS, 'message deleted Successfully')
    return redirect('/previous_appointment')



@login_required
@admin_only
def get_FAQ(request):
    faq = FAQ.objects.all().order_by('-id')
    context = {
        'FAQ': faq,
        'activate_faq': 'active'

    }
    return render(request, 'accounts/get_FAQ.html', context)


@login_required
@admin_only
def FAQ_form(request):
    if request.method == "POST":
        form = FAQForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'FAQ added successfully')
            return redirect("/get_FAQ")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add FAQ')
            return render(request, 'accounts/FAQ_form.html', {'form_FAQ': form})
    context = {
        'form_FAQ': FAQForm,
        'activate_FAQ': 'active'
    }

    return render(request, 'accounts/FAQ_form.html', context)

@login_required
@admin_only
def delete_FAQ(request, FAQ_id):
    faq = FAQ.objects.get(id=FAQ_id)
    faq.delete()
    messages.add_message(request, messages.SUCCESS, 'FAQ deleted Successfully')
    return redirect('/get_FAQ')


@login_required
@admin_only
def FAQ_update_form(request, FAQ_id):
    faq = FAQ.objects.get(id=FAQ_id)
    if request.method == "POST":
        form = FAQForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'FAQ updated successfully')
            return redirect("/get_FAQ")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to update FAQ')
            return render(request, 'accounts/FAQ_update_form.html', {'form_FAQ': form})
    context = {
        'form_FAQ':FAQForm(instance=faq),
        'activate_category': 'active'
    }

    return render(request, 'accounts/FAQ_update_form.html', context)



def about(request):
    faq = FAQ.objects.all().order_by('-id')
    context={
        'FAQ':faq,
        'activate_FAQ':'active'

    }
    return render(request, 'accounts/about.html', context)
