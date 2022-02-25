from django.urls import path
from . import views
urlpatterns = [
    path('dashboard', views.admin_dashboard),

    path('patient', views.show_patient),
    path('doctor', views.show_doctor),
    path('promote/<int:user_id>', views.promote_patient),
    path('demote/<int:user_id>', views.demote_doctor),
    path('delete_user/<int:user_id>', views.delete_user),
    # path('update_user/<int:user_id>', views.update_user),
    # path('view_user', views.get_user),
    path('register',views.register_user),

    path('view_appointment', views.view_appointment),
    path('delete_view_appointment/<int:apt_id>', views.delete_view_appointment),

    path('get_notice', views.get_notice),
    path('add_notice', views.add_notice),
    path('update_notice/<int:notice_id>', views.update_notice),
    path('delete_notice/<int:notice_id>', views.delete_notice),


]