# C:\Users\RoboComlab-00\EmTech\DjangoBackend\project101\registration\urls.py

from django.urls import path
# Using absolute import as previously discussed
from registration import views 

urlpatterns = [
    # POST /api/register/
    path('register/', views.register_user, name='register'),
    
    # POST /api/login/
    path('login/', views.login_user, name='login'),
    
    # GET /api/list/
    path('list/', views.student_list_view, name='student_list'),
    
    # GET, PUT, DELETE /api/1/, /api/2/, etc.
    path('<int:pk>/', views.user_detail, name='user_detail'),
]