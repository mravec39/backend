from rest_framework import generics
from .models import CPU
from .serializers import CPUSerializer


# Create
class CPUListCreateView(generics.ListCreateAPIView):
    queryset = CPU.objects.all()
    serializer_class = CPUSerializer


# Retrieve, Update, Destroy
class CPUDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CPU.objects.all()
    serializer_class = CPUSerializer
