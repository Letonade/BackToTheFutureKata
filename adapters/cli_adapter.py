from core.ports import CartInputPort, CartOutputPort

class CLIInputAdapter(CartInputPort):
    def __init__(self, cart_string):
        self.cart_string = cart_string

    def get_cart(self):
        return self.cart_string.strip().split('\n')
    
    def set_cart(self, new_cart_string):
        self.cart_string = new_cart_string

class CLIOutputAdapter(CartOutputPort):
    def present_total(self, total_price):
        print(f"Total price: {total_price:.2f} €")