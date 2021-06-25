from core.products.product import IProduct


class SweetOnionTopping(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 20
        self.name = 'sweet onion'

    def __str__(self):
        return self.name

    def get_price(self):
        return int(self.price)


class ChiliPepperTopping(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 70
        self.name = 'chili pepper'

    def __str__(self):
        return self.name

    def get_price(self):
        return int(self.price)


class JalapenoTopping(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 50
        self.name = 'jalapeno'

    def __str__(self):
        return self.name

    def get_price(self):
        return int(self.price)