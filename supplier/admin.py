# supplier/admin.py
from django.contrib import admin
from .models import Supplier, Bid

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'user', 'city', 'state', 'business_type', 'wallet_address')
    list_filter = ('state', 'business_type')
    search_fields = ('company_name', 'user__username', 'wallet_address')

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('quote', 'supplier', 'bid_amount', 'status', 'submitted_at')
    list_filter = ('status', 'quote__manufacturer')
    search_fields = ('supplier__company_name', 'quote__product')