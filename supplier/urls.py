from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.supplier_register, name='supplier_register'),
    path('login/', views.supplier_login, name='supplier_login'),
    path('dashboard/', views.supplier_dashboard, name='supplier_dashboard'),
    path('bid/<int:quote_id>/', views.submit_bid, name='submit_bid'),
]