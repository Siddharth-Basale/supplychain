from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import ManufacturerRegistrationForm, ManufacturerLoginForm
from .models import Manufacturer
from django.contrib.auth.models import User

def manufacturer_register(request):
    if request.method == 'POST':
        form = ManufacturerRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1']
            )
            
            manufacturer = Manufacturer.objects.create(
                user=user,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                company_name=form.cleaned_data['company_name'],
                city=form.cleaned_data['city'],
                state=form.cleaned_data['state'],
                business_type=form.cleaned_data['business_type'],
                website=form.cleaned_data['website'],
                phone_number=form.cleaned_data['phone_number'],
                key_products=form.cleaned_data['key_products']
            )
            
            # Log the user in
            auth_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, auth_user)
            return redirect('manufacturer_dashboard')
    else:
        form = ManufacturerRegistrationForm()
    return render(request, 'manufacturer/register.html', {'form': form})

def manufacturer_login(request):
    if request.method == 'POST':
        form = ManufacturerLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # Check if this user is a manufacturer
                try:
                    manufacturer = Manufacturer.objects.get(user=user)
                    login(request, user)
                    return redirect('manufacturer_dashboard')
                except Manufacturer.DoesNotExist:
                    form.add_error(None, "This account is not registered as a manufacturer")
    else:
        form = ManufacturerLoginForm()
    return render(request, 'manufacturer/login.html', {'form': form})

def manufacturer_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('manufacturer_login')
    
    try:
        manufacturer = Manufacturer.objects.get(user=request.user)
        return render(request, 'manufacturer/dashboard.html', {'manufacturer': manufacturer})
    except Manufacturer.DoesNotExist:
        return redirect('manufacturer_login')
    

def request_quote(request):
    if not request.user.is_authenticated:
        return redirect('manufacturer_login')
    return render(request, 'manufacturer/request_quote.html', {
        'manufacturer': Manufacturer.objects.get(user=request.user)
    })

def list_products(request):
    if not request.user.is_authenticated:
        return redirect('manufacturer_login')
    return render(request, 'manufacturer/list_products.html', {
        'manufacturer': Manufacturer.objects.get(user=request.user)
    })

def complete_profile(request):
    if not request.user.is_authenticated:
        return redirect('manufacturer_login')
    return render(request, 'manufacturer/complete_profile.html', {
        'manufacturer': Manufacturer.objects.get(user=request.user)
    })