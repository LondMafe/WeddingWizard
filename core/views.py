from django.shortcuts import render, redirect
from django.contrib.auth import logout
from item.models import Category, Item
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignupForm, SignupVendorsForm, EmailUpdateForm

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def services(request):
    items = Item.objects.filter(is_available=True)[0:6]
    categories = Category.objects.all()
    
    return render(request, 'core/services.html', {
        'categories': categories,
        'items': items,  
    })
    
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
    else:
        form = SignupForm()
    
    return render(request, 'core/signup.html', {
        'form': form,
    })
    
def signupVendors(request):
    if request.method == 'POST':
        form = SignupVendorsForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
    else:
        form = SignupVendorsForm()
        
    return render(request, 'core/signupVendors.html', {
        'form': form,
    })

@login_required
def profile(request):
    profile = request.user.profile 
    if request.method == 'POST':
        form = EmailUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirigir al inicio tras actualizar
    else:
        form = EmailUpdateForm(instance=request.user)

    return render(request, 'core/profile.html', {'form': form, 'profile': profile})

@login_required
def deleteAccount(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        logout(request)
        messages.success(request, 'Your account has been deleted!')
        return redirect('/')
    return render(request, 'core/deleteAccount.html')