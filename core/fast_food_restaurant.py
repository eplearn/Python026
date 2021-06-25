from core.client import Client
from core.ingredients import IngredientData
from core.hot_dog import Cook
from core.hot_dog import HotDog


class RestaurantFacade:
    """
    Фасад закусочной
    """

    def __init__(self):
        self.cook = Cook()  # В ресторане есть "повар", который на самом деле Директор
        self.available_ingredients = IngredientData()

    def cook_hot_dog(self, hot_dog: str) -> HotDog:
        """
        Возвращает готовый хот-дог
        """
        return self.cook.make_hot_dog(hot_dog)

    def make_order(self, client, hot_dog):
        """
        Обрабатывает заказ клиента
        """
        hot_dog = self.cook.make_hot_dog(hot_dog)
        if client.get_money() >= hot_dog.get_price():
            return hot_dog
        else:
            return f'has no money enough to order hot-dog {hot_dog}.'
