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
    
    def add(self, item, quantity):
        # Get the item id
        product_id = str(item.id)
        
        # Get the quantity
        product_qty = str(quantity)
        
        # Logic
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(item.price)}
            self.cart[product_id] = int(product_qty)
            
        self.session.modified = True
      
    def cartTotal(self):
        # Get ids from cart
        product_ids = self.cart.keys()
        # Lookup the keys in the database
        items = Item.objects.filter(id__in=product_ids)
        # Get quantities
        quantities = self.cart
        
        # Start counting at 0
        total = 0
        
        for key, value in quantities.items():
            key = int(key)
            for item in items:
                if item.id == key:
                    total = total + (item.price * value)
        return total
        
        
        
        
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
    
    def getQuantities(self):
        quantities = self.cart
        return quantities
    
    def cartUpdate(self, item, quantity):
        product_id = str(item)
        product_qty = int(quantity)
        
        # Get cart
        theCart = self.cart
        
        # Update dictionary / cart
        theCart[product_id] = product_qty
        
        self.session.modified = True
        
        thing = self.cart
        return thing
    
    def cartDelete(self, item):
        product_id = str(item)
        
        # Delete item from cart
        if product_id in self.cart:
            del self.cart[product_id]
        
        self.session.modified = True