# supplychain/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('manufacturer/', include('manufacturer.urls')),
    path('supplier/', include('supplier.urls')),
]