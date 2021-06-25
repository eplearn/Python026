from core.products.product import IProduct


class Mayonnaise(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 70
        self.name = 'mayonnaise'

    def __str__(self):
        return self.name

    def get_price(self):
        return int(self.price)


class Ketchup(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 50
        self.name = 'ketchup'

    def __str__(self):
        return self.name

    def get_price(self):
        return int(self.price)


class Mustard(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 30
        self.name = 'mustard'

    def __str__(self):
        return self.name

    def get_price(self):
        return int(self.price)
