
from django.urls import path, include

urlpatterns = [
    path('news/', include('news.urls')),
    path('admins/', include('admins.urls')),
    path('', include('accounts.urls')),
    path('doctor/', include('doctor.urls')),
    path('doc/', include('doc.urls')),
]
