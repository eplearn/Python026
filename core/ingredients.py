"""
Здесь находятся фабрики ингредиентов и класс, содержащий словарь ингредиентов.
"""

from abc import ABC, abstractmethod

from core.products.product import IProduct
from core.products.sauce import Ketchup
from core.products.sauce import Mayonnaise
from core.products.sauce import Mustard
from core.products.topping import JalapenoTopping
from core.products.topping import SweetOnionTopping
from core.products.topping import ChiliPepperTopping


class Ingredients(ABC):
    """
    Абстрактное описание фабрики ингредиентов
    """

    @abstractmethod
    def create_ingredient(self, ingredient: str) -> IProduct:
        ...


class IngredientData:
    def __init__(self):
        self.name = 'добавки и соусы'
        self.data = {'добавки': ['лук', 'халапеньо', 'чили'],
                     'соусы': ['майонез', 'кетчуп', 'горчица']}

    def get_name(self):
        return self.name

    def get_data(self):
        return self.data


class SauceIngredient(Ingredients):
    """
    Фабрика соусов
    """

    def create_ingredient(self, ingredient: str) -> IProduct:
        if ingredient == 'майонез':
            return Mayonnaise()
        elif ingredient == 'кетчуп':
            return Ketchup()
        elif ingredient == 'горчица':
            return Mustard()


class ToppingIngredient(Ingredients):
    """
    Фабрика добавок
    """

    def create_ingredient(self, ingredient: str) -> IProduct:
        if ingredient == 'халапеньо':
            return JalapenoTopping()
        elif ingredient == 'чили':
            return ChiliPepperTopping()
        elif ingredient == 'лук':
            return SweetOnionTopping()
