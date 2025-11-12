# C:\Users\RoboComlab-00\EmTech\DjangoBackend\project101\registration\views.py

from django.shortcuts import render

# Import necessary Django REST Framework (DRF) components
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Import models and serializers from the current app
from .models import UserRegistration
from .serializer import UserRegistrationSerializer


@api_view(['POST'])
def register_user(request):
    """
    Handles user registration (creation of a new user).
    """
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_user(request):
    """
    Placeholder for the user login view. 
    You will add authentication (e.g., token generation) logic here.
    """
    # For now, just return a simple message to confirm the URL works
    return Response({"message": "Login endpoint reached! Add your authentication logic here."}, 
                    status=status.HTTP_200_OK)


@api_view(['GET'])
def student_list_view(request):
    """
    Returns a list of all registered users/students.
    """
    users = UserRegistration.objects.all()
    serializer = UserRegistrationSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET','PUT', 'DELETE'])
def user_detail(request, pk):
    """
    Retrieve, update, or delete a single user instance.
    """
    try:
        user = UserRegistration.objects.get(pk=pk)
    except UserRegistration.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserRegistrationSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserRegistrationSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print("serializer errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)