from django.shortcuts import render, redirect

from item.models import Category, Item

from .forms import SignupForm

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