from django.shortcuts import render, get_object_or_404
from .cart import Cart
from item.models import Item
from django.http import JsonResponse

# Create your views here.

def cartDetail(request):
    # Get the cart
    cart = Cart(request)
    cartItems = cart.getItems
    return render(request, 'cart/cartDetail.html', {"cartItems": cartItems })

def cartAdd(request):
    # Get the cart
    cart = Cart(request)
    # Test for POST
    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))
        
        # Lookup the item in the database
        item = get_object_or_404(Item, id=product_id)
        
        # Save the item to the cart (to the session)
        cart.add(item=item)
        
        # Get cart quantity
        cartQuantity = cart.__len__()
        
        # Return a JSON response
        # response = JsonResponse({'Item name': item.name})
        response = JsonResponse({'Quantity': cartQuantity})
        return response
        

def cartDelete(request):
    pass