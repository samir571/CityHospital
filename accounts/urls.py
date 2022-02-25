from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns =[
    # path('', views.homepage),
    path('about', views.about, name="about"),
    path('doctor', views.doctor),
    path('news', views.news),
    path('contact', views.contact_form,name="contact_form"),
    path('login', views.login_user),
    path('register', views.register_user),
    path('logout', views.logout_user),
    path('', views.home_news, name="home_news"),
    path('profile', views.profile),
    path('update_profile', views.update_profile),

    path('delete_contact/<int:contact_id>', views.delete_contact, name="delete_contact"),
    path('view_contact', views.get_contact),
    path('change_password', views.change_password),

    path('change_user_password', views.change_user_password),

    path('previous_appointment', views.my_appointments),
    path('delete_previous_appointment/<int:apt_id>', views.delete_my_appointments),

    path('get_FAQ', views.get_FAQ, name="get_FAQ"),
    path('FAQ_form', views.FAQ_form),
    path('delete_FAQ/<int:FAQ_id>', views.delete_FAQ),
    path('update_FAQ/<int:FAQ_id>', views.FAQ_update_form),

    # path('delete_previous_appointment/<int:appointment_id>', views.delete_appointment),


    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name='password_reset_complete'),

]