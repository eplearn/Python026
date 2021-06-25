class Goods:
    """
    Интерфейс товара
    """

    def __init__(self):
        self.name = None
        self.ingredients = []
        self.price = None

    def __str__(self):
        return self.name
