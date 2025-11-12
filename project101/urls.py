# project101/project101/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # FIX: Change 'student_api.urls' to 'registration.urls'
    path('api/', include('registration.urls')), 
]