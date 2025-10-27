# signup/urls.py

from django.urls import path
from .views import RegistrationView, api_root # Import both the view and the new temporary root view

urlpatterns = [
    # 1. FIX for the 404 Error: Defines a view for the root path (http://127.0.0.1:8000/)
    path('', api_root, name='api-root'), 
    
    # 2. API Endpoint for Registration (The one your React Native app hits)
    # Complete URL: http://127.0.0.1:8000/api/register/
    path('api/register/', RegistrationView.as_view(), name='api-register'),
    
    # You could add a login endpoint here too:
    # path('api/login/', LoginView.as_view(), name='api-login'),
]