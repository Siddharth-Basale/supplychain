from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.manufacturer_register, name='manufacturer_register'),
    path('login/', views.manufacturer_login, name='manufacturer_login'),
    path('dashboard/', views.manufacturer_dashboard, name='manufacturer_dashboard'),
]