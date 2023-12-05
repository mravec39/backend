from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import viewsets, generics
from rest_framework.authtoken.models import Token
from . import models
from . import serializers
from .models import CustomUser
from .serializers import CustomUserSerializer, RegistrationSerializer, LoginSerializer
from django.db import IntegrityError
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny


@api_view(['POST'])
@permission_classes([AllowAny])
# @csrf_exempt
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    email = serializer.validated_data['email']
    password = serializer.validated_data['password']

    user = authenticate(request, username=email, password=password)

    if user:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return JsonResponse({'token': token.key, 'message': 'Login successful'})
    else:
        return JsonResponse({'error': 'Login failed! Email or Password wrong'}, status=status.HTTP_401_UNAUTHORIZED)


User = get_user_model()


@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def registration_view(request):
    serializer = RegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    email = serializer.validated_data['email']
    password = serializer.validated_data['password']
    password_confirmation = serializer.validated_data['password_confirmation']

    if password != password_confirmation:
        return Response({'error': 'Password and confirmation do not match'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.create_user(email=email, password=password)
        return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)
    except IntegrityError:
        return Response({'error': 'Error creating user'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UsersView(viewsets.ReadOnlyModelViewSet):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.CustomUserSerializer


# Create
class CustomUserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


# Retrieve, Update, Destroy
class CustomUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
