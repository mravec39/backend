from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from . import models
from . import serializers
from .models import CustomUser
from .serializers import CustomUserSerializer
from django.db import IntegrityError
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')
        remember_me = request.data.get('rememberMe')

        user = authenticate(request, username=email, password=password)

        if user:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)


User = get_user_model()


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
@csrf_exempt
def registration_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')


    if User.objects.filter(email=email).exists():
        return Response({'error': 'Email is already registered'}, status=status.HTTP_400_BAD_REQUEST)

    # Kontrola, zda se heslo shoduje s potvrzením hesla
    if password != password_confirmation:
        return Response({'error': 'Password and confirmation do not match'}, status=status.HTTP_400_BAD_REQUEST)

    # Vytvoření uživatele
    try:
        user = User.objects.create_user(email=email, password=password)
        return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)
    except IntegrityError:
        return Response({'error': 'Error creating user'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UsersView(viewsets.ReadOnlyModelViewSet):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.CustomUserSerializer


class CustomUserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
