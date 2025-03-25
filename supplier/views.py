from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import SupplierRegistrationForm, SupplierLoginForm, BidForm
from .models import Supplier, Bid
from django.contrib.auth.models import User
from manufacturer.models import QuoteRequest
from django.contrib import messages

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
    

def supplier_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('supplier_login')
    
    try:
        supplier = Supplier.objects.get(user=request.user)
        open_quotes = QuoteRequest.objects.filter(status='open').order_by('-created_at')
        your_bids = Bid.objects.filter(supplier=supplier).select_related('quote')
        
        return render(request, 'supplier/dashboard.html', {
            'supplier': supplier,
            'open_quotes': open_quotes,
            'your_bids': your_bids
        })
    except Supplier.DoesNotExist:
        return redirect('supplier_login')

def submit_bid(request, quote_id):
    if not request.user.is_authenticated:
        return redirect('supplier_login')
    
    supplier = get_object_or_404(Supplier, user=request.user)
    quote = get_object_or_404(QuoteRequest, id=quote_id, status='open')
    
    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            Bid.objects.create(
                supplier=supplier,
                quote=quote,
                bid_amount=form.cleaned_data['bid_amount'],
                delivery_time=form.cleaned_data['delivery_time'],
                comments=form.cleaned_data['comments']
            )
            messages.success(request, 'Your bid has been submitted successfully!')
            return redirect('supplier_dashboard')
    else:
        form = BidForm()
    
    return render(request, 'supplier/submit_bid.html', {
        'form': form,
        'quote': quote,
        'supplier': supplier
    })