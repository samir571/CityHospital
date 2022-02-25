from django.shortcuts import render, redirect
from .forms import CategoryForm, DoctorForm
from django.contrib import messages
from .models import Category, Doctor
from accounts.auth import admin_only, user_only
from django.contrib.auth.decorators import login_required
import os
from accounts.forms import AppointmentForm
from accounts.models import Appointment


@login_required
@admin_only
def category_form(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Category added successfully')
            return redirect("/doctor/get_category")
        else:
            messages.add_message(request, messages.ERROR,'Unable to add category')
            return render(request, 'doctor/category_form.html',{'form_category':form})
    context={
        'form_category' : CategoryForm,
        'activate_category':'active'
    }

    return render(request, 'doctor/category_form.html', context)


@login_required
@admin_only
def get_category(request):
    categories = Category.objects.all().order_by('-id')
    context={
        'categories': categories,
        'activate_category' :'active'

    }
    return render(request, 'doctor/get_category.html',context)


@login_required
@admin_only
def delete_category(request, category_id):
    category=Category.objects.get(id=category_id)
    category.delete()
    messages.add_message(request, messages.SUCCESS,'Category deleted Successfully')
    return redirect('/doctor/get_category')


@login_required
@admin_only
def category_update_form(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Category updated successfully')
            return redirect("/doctor/get_category")
        else:
            messages.add_message(request, messages.ERROR,'Unable to update category')
            return render(request, 'doctor/category_update_form.html',{'form_category':form})
    context={
        'form_category' : CategoryForm(instance=category),
        'activate_category':'active'
    }

    return render(request, 'doctor/category_update_form.html', context)


# _______________________Doctor PART______________________________
@login_required
@admin_only
def doctor_form(request):
    if request.method == "POST":
        form = DoctorForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Doctor added successfully')
            return redirect("/doctor/get_doctor")
        else:
            messages.add_message(request, messages.ERROR,'Unable to add doctor')
            return render(request, 'doctor/doctor_form.html',{'form_doctor':form})
    context={
        'form_doctor' : DoctorForm,
        'activate_doctor':'active'
    }

    return render(request, 'doctor/doctor_form.html', context)

@login_required
@admin_only
def get_doctor(request):
    news = Doctor.objects.all().order_by('-id')
    context={
        'doctor': news,
        'activate_doctor' :'active'

    }
    return render(request, 'doctor/get_doctor.html',context)

@login_required
@admin_only
def delete_doctor(request, doctor_id):
    doctor=Doctor.objects.get(id=doctor_id)
    os.remove(doctor.doctor_image.path)
    doctor.delete()
    messages.add_message(request, messages.SUCCESS,'Doctor deleted Successfully')
    return redirect('/doctor/get_doctor')

@login_required
@admin_only
def doctor_update_form(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    if request.method == "POST":
        if request.FILES.get('doctor_image'):
            os.remove(doctor.doctor_image.path)
        form = DoctorForm(request.POST,request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Doctor updated successfully')
            return redirect("/doctor/get_doctor")
        else:
            messages.add_message(request, messages.ERROR,'Unable to update doctor')
            return render(request, 'doctor/doctor_update_form.html',{'form_doctor':form})
    context={
        'form_doctor' : DoctorForm(instance=doctor),
        'activate_doctor':'active'
    }

    return render(request, 'doctor/doctor_update_form.html', context)


def show_categories(request):
    categories = Category.objects.all().order_by('-id')
    context={
        'categories':categories,
        'activate_category_user': 'active'

    }
    return render(request, 'doctor/show_categories.html', context)


@login_required
def appointment_form(request):
    user = request.user
    doctor = Doctor.objects.all().order_by('-id')
    if request.method == "POST":
        data = request.POST
        form = AppointmentForm(request.POST)

        if form.is_valid():
            category = Category.objects.get(id=data['category'])
            Appointment.objects.create(full_name = data['full_name'],
                                       email = data['email'],
                                       address = data['address'],
                                       age = data['age'],
                                       gender = data['gender'],
                                       number = data['number'],
                                       date = data['date'],
                                       category = category,
                                       user = user,
                                       message = data['message'])
            messages.add_message(request, messages.SUCCESS, 'appointment requested successfully')
            return redirect("/doctor/get_doctor_user")
        else:
            messages.add_message(request, messages.ERROR,'Unable to request appointment')
            return render(request, 'doctor/show_doctor.html',{'appointment_form':form})
    context={
        'appointment_form' : AppointmentForm,
        'activate_appointment':'active',

        'doctor': doctor,
        'activate_doctor_user': 'active',
    }

    return render(request, 'doctor/show_doctor.html', context)






