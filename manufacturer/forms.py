from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ManufacturerRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    company_name = forms.CharField(max_length=200, required=True)
    city = forms.CharField(max_length=100, required=True)
    state = forms.CharField(max_length=100, required=True)
    business_type = forms.CharField(max_length=100, required=True)
    website = forms.URLField(required=False)
    phone_number = forms.CharField(max_length=20, required=True)
    key_products = forms.CharField(widget=forms.Textarea, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',
                  'first_name', 'last_name', 'company_name', 'city', 
                  'state', 'business_type', 'website', 'phone_number', 
                  'key_products')

class ManufacturerLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    
# In manufacturer/views.py, change the import to:
from supplier.forms import FeedbackForm  # Instead of importing from manufacturer.forms
    
# In manufacturer/forms.py
from django import forms

class FeedbackForm(forms.Form):
    # Define choices here instead of referencing model
    RATING_CHOICES = [
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    ]
    
    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.RadioSelect,
        required=True
    )
    comments = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4}),
        required=True,
        label='Your Feedback'
    )