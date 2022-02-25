from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from accounts.forms import LoginForm, ContactForm, AppointmentForm
from accounts.forms import LoginForm
from accounts.auth import unauthenticated_user,admin_only,user_only,doctor_only
from django.contrib.auth.decorators import login_required
from accounts.models import Contact_Us, Appointment
from news.models import News
from.models import Notice
from.forms import NoticeForm



@login_required
@admin_only
def admin_dashboard(request):
    patient = User.objects.filter(is_staff=0)
    patient_count = patient.count()
    doctor = User.objects.filter(is_staff=1)
    doctor_count = doctor.count()
    message = Contact_Us.objects.all()
    message_count = message.count()
    news = News.objects.all()
    news_count = news.count()
    appointment = Appointment.objects.all()
    appointment_count = appointment.count()

    context = {
        'patient': patient_count,
        'users': patient_count+doctor_count,
        'doctor': doctor_count,
        'message': message_count,
        'news': news_count,
        'appointment': appointment_count,

    }
    return render(request, 'admins/dashboard.html', context)


@login_required
@admin_only
def show_patient(request):
    users = User.objects.filter(is_staff=0).order_by('-id')
    context = {
        'users': users
    }
    return render(request, 'admins/patient.html', context)


@login_required
@admin_only
def show_doctor(request):
    doctors = User.objects.filter(is_staff=1).order_by('-id')
    context = {
        'doctors': doctors
    }
    return render(request, 'admins/doctor.html', context)


@login_required
@admin_only
def promote_patient(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_staff = True
    user.save()
    messages.add_message(request, messages.SUCCESS, 'User Promoted To Doctor')
    return redirect('/admins/doctor')


@login_required
@admin_only
def demote_doctor(request, user_id):
    admin = User.objects.get(id=user_id)
    admin.is_staff = False
    admin.save()
    messages.add_message(request, messages.SUCCESS, 'Dcotor Demoted To Patient')
    return redirect('/admins/patient')



# Notice Doctors
@login_required
@admin_only
def get_notice(request):
    notice = Notice.objects.all().order_by('-id')
    context = {
        'notice': notice,
    }
    return render(request, 'admins/get_notice.html', context)


@login_required
@admin_only
def delete_notice(request, notice_id):
    notice = Notice.objects.get(id=notice_id)
    notice.delete()
    messages.add_message(request, messages.SUCCESS, 'Notice deleted successfully')
    return redirect('/admins/get_notice')


@login_required
@admin_only
def add_notice(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Notice added successfully')
            return redirect("/admins/get_notice")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add notice')
            return render(request, 'admins/add_notice.html', {'form_notice': form})
    context = {
        'form_notice': NoticeForm,

    }
    return render(request, 'admins/add_notice.html', context)


@login_required
@admin_only
def update_notice(request, notice_id):
    notice = Notice.objects.get(id=notice_id)
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES, instance=notice)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Notice updated successfully')
            return redirect("/admins/get_notice")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to update Notice')
            return render(request, 'admins/update_notice.html', {'form_notice': form})
    context = {
        'form_notice': NoticeForm(instance=notice),

    }
    return render(request, 'admins/update_notice.html', context)



@login_required
@admin_only
def view_appointment(request):
    user = request.user
    print(user)
    appointments = Appointment.objects.order_by('-id')
    context = {
        'appointments':appointments,
    }
    return render(request, 'admins/view_appointment.html', context)

@login_required
@admin_only
def delete_view_appointment(request, apt_id):
    appointments = Appointment.objects.get(id=apt_id)
    appointments.delete()
    messages.add_message(request, messages.SUCCESS, 'message deleted Successfully')
    return redirect('/admins/view_appointment')


@login_required
@admin_only
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.save()

            messages.add_message(request, messages.SUCCESS, "User Registered Successfully")
            return redirect('/admins/patient')
        else:
            messages.add_message(request, messages.ERROR, "Unable To Register User")
            return render(request, 'admins/register_user.html', {'form_register': form})
    context = {
        'form_register': UserCreationForm,
    }
    return render(request, 'admins/register_user.html', context)



@login_required
@admin_only
def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    messages.add_message(request, messages.SUCCESS, 'User deleted successfully')
    return redirect('/admins/patient')
# @login_required
# @admin_only
# def get_user(request):
#     user = Login.objects.all().order_by('-id')
#     context={
#         'user': user,
#     }
#     return render(request, 'admins/view_user.html',context)
#
# @login_required
# @admin_only
# def delete_user(request, user_id):
#     contact=Login.objects.get(id=user_id)
#     contact.delete()
#     messages.add_message(request, messages.SUCCESS,'user deleted Successfully')
#     return redirect('/admins/view_user')


# @login_required
# @admin_only
# def update_user(request, user_id):
#     user = LoginForm.objects.get(id=user_id)
#     if request.method == "POST":
#         form = LoginForm(request.POST,instance=user)
#         if form.is_valid():
#             form.save()
#             messages.add_message(request, messages.SUCCESS, 'User updated successfully')
#             return redirect("/admins/get_user")
#         else:
#             messages.add_message(request, messages.ERROR,'Unable to update user')
#             return render(request, 'news/category_update_form.html',{'form_category':form})
#     context={
#         'form_category' : CategoryForm(instance=category),
#         'activate_category':'active'
#     }
#
#     return render(request, 'news/category_update_form.html', context)



