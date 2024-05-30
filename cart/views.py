from django.shortcuts import render, get_object_or_404
from .cart import Cart
from item.models import Item
from django.http import JsonResponse

# Create your views here.

def cartDetail(request):
    # Get the cart
    cart = Cart(request)
    cartItems = cart.getItems
    quantities = cart.getQuantities
    return render(request, 'cart/cartDetail.html', {"cartItems": cartItems, "quantities": quantities})

def cartAdd(request):
    # Get the cart
    cart = Cart(request)
    # Test for POST
    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        
        # Lookup the item in the database
        item = get_object_or_404(Item, id=product_id)
        
        # Save the item to the cart (to the session)
        cart.add(item=item, quantity=product_qty)
        
        # Get cart quantity
        cartQuantity = cart.__len__()
        
        # Return a JSON response
        # response = JsonResponse({'Item name': item.name})
        response = JsonResponse({'Quantity': cartQuantity})
        return response
        

def cartDelete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))
        
        # Call delete method
        cart.cartDelete(item = product_id)
        
        response = JsonResponse({'item': 'product_id'})
        return response

def cartUpdate(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.cartUpdate(item = product_id, quantity = product_qty)
        
        response = JsonResponse({'qty': 'product_qty'})
        return response