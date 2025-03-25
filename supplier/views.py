from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SupplierRegistrationForm, SupplierLoginForm
from .models import Supplier
from django.contrib.auth.models import User

def supplier_register(request):
    if request.method == 'POST':
        form = SupplierRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1']
            )
            
            supplier = Supplier.objects.create(
                user=user,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                company_name=form.cleaned_data['company_name'],
                city=form.cleaned_data['city'],
                state=form.cleaned_data['state'],
                business_type=form.cleaned_data['business_type'],
                website=form.cleaned_data['website'],
                phone_number=form.cleaned_data['phone_number'],
                key_services=form.cleaned_data['key_services']
            )
            
            # Log the user in
            auth_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, auth_user)
            return redirect('supplier_dashboard')
    else:
        form = SupplierRegistrationForm()
    return render(request, 'supplier/register.html', {'form': form})

def supplier_login(request):
    if request.method == 'POST':
        form = SupplierLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # Check if this user is a supplier
                try:
                    supplier = Supplier.objects.get(user=user)
                    login(request, user)
                    return redirect('supplier_dashboard')
                except Supplier.DoesNotExist:
                    form.add_error(None, "This account is not registered as a supplier")
    else:
        form = SupplierLoginForm()
    return render(request, 'supplier/login.html', {'form': form})

def supplier_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('supplier_login')
    
    try:
        supplier = Supplier.objects.get(user=request.user)
        return render(request, 'supplier/dashboard.html', {'supplier': supplier})
    except Supplier.DoesNotExist:
        return redirect('supplier_login')