from django.urls import path
from .views import CPUDetailView, CPUListCreateView

urlpatterns = [
    path('cpus/', CPUListCreateView.as_view(), name='cpu-list-create'),
    path('cpus/<int:pk>/', CPUDetailView.as_view(), name='cpu-detail'),
]