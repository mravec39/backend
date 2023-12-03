from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.decorators import authentication_classes, permission_classes

from .models import CPU
from .serializers import CPUSerializer


# Create your views here.

class CPUListCreateView(generics.ListCreateAPIView):
    queryset = CPU.objects.all()
    serializer_class = CPUSerializer


class CPUDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CPU.objects.all()
    serializer_class = CPUSerializer
