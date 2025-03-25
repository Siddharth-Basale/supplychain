from django.urls import path
from . import views

urlpatterns = [
    # Authentication URLs
    path('register/', views.manufacturer_register, name='manufacturer_register'),
    path('login/', views.manufacturer_login, name='manufacturer_login'),
    
    # Dashboard and Action URLs
    path('dashboard/', views.manufacturer_dashboard, name='manufacturer_dashboard'),
    path('request-quote/', views.request_quote, name='manufacturer_request_quote'),
    path('list-products/', views.list_products, name='manufacturer_list_products'),
    path('complete-profile/', views.complete_profile, name='manufacturer_complete_profile'),
    path('quote-history/', views.quote_history, name='manufacturer_quote_history'),
    path('profile/', views.view_profile, name='manufacturer_profile'),
    path('profile/edit/', views.edit_profile, name='manufacturer_edit_profile'),
]