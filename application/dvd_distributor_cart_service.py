from core.dvd_distributor import DvdDistributor
from core.ports import CartInputPort, CartOutputPort

class DvdDistributorCartService:
    def __init__(self, cart_input_port: CartInputPort, cart_output_port: CartOutputPort, dvd_distributor: DvdDistributor):
        self.cart_input_port = cart_input_port
        self.cart_output_port = cart_output_port
        self.dvd_distributor = dvd_distributor

    def parse_cart(self, cart_items):
        saga_dvds = [item for item in cart_items if self.dvd_distributor.SAGA_TITLE in item]
        other_dvds = [item for item in cart_items if self.dvd_distributor.SAGA_TITLE not in item]
        return saga_dvds, other_dvds

    def calculate_price(self, saga_dvds, other_dvds):
        saga_count = len(saga_dvds)
        total_price = 0

        if saga_count == 1:
            total_price += self.dvd_distributor.get_saga_price()
        elif saga_count == 2:
            total_price += (self.dvd_distributor.get_saga_price() * saga_count) * (1 - self.dvd_distributor.get_discounts()[2])
        elif saga_count >= 3:
            total_price += (self.dvd_distributor.get_saga_price() * saga_count) * (1 - self.dvd_distributor.get_discounts()[3])

        total_price += self.dvd_distributor.get_other_dvd_price() * len(other_dvds)

        return total_price

    def handle_cart(self):
        cart_items = self.cart_input_port.get_cart()
        total_price = 0.00
        
        if cart_items and not cart_items[0] == "": 
            saga_dvds, other_dvds = self.parse_cart(cart_items)
            total_price = self.calculate_price(saga_dvds, other_dvds)
        
        self.cart_output_port.present_total(total_price)
        return total_price
