from core.products.product import IProduct


class Roll(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 100
        self.name = 'roll'

    def __str__(self):
        return self.name

    def get_price(self):
        return int(self.price)
