# manufacturer/admin.py
from django.contrib import admin
from .models import Manufacturer, QuoteRequest

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'user', 'city', 'state', 'business_type')
    list_filter = ('state', 'business_type')
    search_fields = ('company_name', 'user__username')

@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('product', 'manufacturer', 'status', 'deadline', 'created_at')
    list_filter = ('status', 'category')
    search_fields = ('product', 'manufacturer__company_name')