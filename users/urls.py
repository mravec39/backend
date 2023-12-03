# users/urls.py
from django.urls import path
from .views import CustomUserListCreateView, CustomUserDetailView
from .views import login_view
from .views import registration_view

urlpatterns = [
    path('users/', CustomUserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', CustomUserDetailView.as_view(), name='user-detail'),
    path('login/', login_view, name='login'),
    path('registration/', registration_view, name='registration')
]