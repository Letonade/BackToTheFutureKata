from abc import ABC, abstractmethod

class CartInputPort(ABC):
    @abstractmethod
    def get_cart(self):
        pass

class CartOutputPort(ABC):
    @abstractmethod
    def present_total(self, total_price):
        pass