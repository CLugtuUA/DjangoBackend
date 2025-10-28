# signup/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse 
from .serializers import UserSerializer

# ----------------------------------------------------------------------
# 1. API ROOT VIEW (Confirms server is running at http://127.0.0.1:8000/)
# ----------------------------------------------------------------------
def api_root(request):
    """Simple view to confirm the API is running."""
    return JsonResponse({'message': 'Welcome to the Django API root. The server is working!', 'status': 'ok'})


# ----------------------------------------------------------------------
# 2. REGISTRATION API VIEW (Handles POST request)
# ----------------------------------------------------------------------
class RegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)