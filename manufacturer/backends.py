from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from .models import Manufacturer
from django.contrib.auth import get_user_model

class ManufacturerBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel._default_manager.get(username=username)
            
            # Check if user is a manufacturer and not staff/admin
            if user.check_password(password) and not user.is_staff:
                try:
                    Manufacturer.objects.get(user=user)
                    return user
                except Manufacturer.DoesNotExist:
                    return None
        except UserModel.DoesNotExist:
            return None