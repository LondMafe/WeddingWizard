from item.models import Item

class Cart():
    def __init__(self, request):
        self.session = request.session
        
        # Get the current session key if it exists
        cart = self.session.get('session_key') 
        
        # If the user is new, create a new session key
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
            
        # Make sure the cart is available on all pages of the site
        self.cart = cart
    
    def add(self, item):
        # Get the item id
        product_id = str(item.id)
        
        # Logic
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(item.price)}
            
        self.session.modified = True
        
    # Get how many things are in the cart
    def __len__(self):
        return len(self.cart)
    
    # See what's in the cart
    def getItems(self):
        # Get ids from cart
        product_ids = self.cart.keys()
        
        # Use ids to lookup products in db
        items = Item.objects.filter(id__in=product_ids)
        
        # Return those products
        return items