from django.urls import path
from . import views

urlpatterns = [
    path('category_form', views.category_form),
    path('get_category', views.get_category),
    path('delete_category/<int:category_id>', views.delete_category),
    path('update_category/<int:category_id>', views.category_update_form),


    path('doctor_form', views.doctor_form),
    path('get_doctor', views.get_doctor),
    path('delete_doctor/<int:doctor_id>', views.delete_doctor),
    path('update_doctor/<int:doctor_id>', views.doctor_update_form),


    path('get_category_user', views.show_categories),
    path('get_doctor_user', views.appointment_form),


]
