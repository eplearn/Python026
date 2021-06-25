class Client:
    """Класс клиента"""

    def __init__(self, name, money):
        self.name = name
        self.money = int(money)
        self.orders = []

    def get_name(self):
        """Возвращает имя"""
        return self.name

    def get_money(self):
        """Возвращает текущее количество денег"""
        return self.money

    def get_orders(self):
        """Возвращает имя"""
        return self.orders
