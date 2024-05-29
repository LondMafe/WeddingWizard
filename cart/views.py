from django.shortcuts import render

# Create your views here.

def cartDetail(request):
    return render(request, 'cart/cartDetail.html', {})

def cartAdd(request):
    pass

def cartDelete(request):
    pass