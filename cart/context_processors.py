from .cart import Cart

# Create context processor to make the cart available on all pages
def cart(request):
    # Return the data from the cart
    return {'cart': Cart(request)}