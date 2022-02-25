
from django.urls import path, include
from . import views
urlpatterns = [
    path('dashboard', views.dashboard),
    path('news', views.show_news),
    path('categories', views.show_categories),
    path('profile', views.profile),
    path('update_profile', views.update_profile),

    path('change_doc_password', views.change_doc_password),

    path('total_appointment', views.my_appointments),
    path('show_notice', views.show_notice),
]
