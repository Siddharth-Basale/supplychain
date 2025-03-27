# supplychain/admin.py (create this file if it doesn't exist)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from manufacturer.models import Manufacturer
from supplier.models import Supplier

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'user_type')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')

    def user_type(self, obj):
        if Manufacturer.objects.filter(user=obj).exists():
            return "Manufacturer"
        elif Supplier.objects.filter(user=obj).exists():
            return "Supplier"
        return "Regular User"
    user_type.short_description = 'User Type'

# Unregister the default User admin and register our custom one
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)