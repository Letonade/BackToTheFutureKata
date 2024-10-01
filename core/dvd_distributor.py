class DvdDistributor:
    SAGA_PRICE = 15
    OTHER_DVD_PRICE = 20
    DISCOUNTS = {2: 0.10, 3: 0.20}
    SAGA_TITLE = "Back to the Future"

    def __init__(self):
        pass

    def get_saga_price(self):
        return self.SAGA_PRICE

    def get_other_dvd_price(self):
        return self.OTHER_DVD_PRICE

    def get_discounts(self):
        return self.DISCOUNTS