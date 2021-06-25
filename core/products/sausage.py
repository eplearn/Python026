from core.products.product import IProduct


class Sausage(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 300
        self.name = 'sausage'

    def __str__(self):
        return self.name

    def get_price(self):
        return int(self.price)
