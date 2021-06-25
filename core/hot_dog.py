from core.goods import Goods
from core.products.roll import Roll
from core.products.sausage import Sausage
from core.ingredients import SauceIngredient
from core.ingredients import ToppingIngredient
from core.products.product import IProduct


class HotDog(Goods):
    def __init__(self, name):
        super().__init__()
        self.name = name
        roll = Roll()
        sausage = Sausage()
        self.ingredients = []
        self.ingredients.append(roll)
        self.ingredients.append(sausage)
        self.initial_price = roll.get_price() + sausage.get_price()

    def __str__(self):
        return f"{self.name}: {', '.join(map(str, self.ingredients))} for {self.get_price()} shekels"

    def get_price(self):
        total_price = self.initial_price
        for ingredient in self.ingredients[2:]:
            total_price += ingredient.price
        return total_price

    def get_name(self):
        return self.name

    def add_ingredient(self, ingredient: IProduct) -> None:
        self.ingredients.append(ingredient)


class HotDogBuilder:
    """
    Строитель хот-дога. На его основе создаются конкретные строители хот-дога,
    которые содержат в себе методы, собирающие ход-доги в правильной последовательности.
    """

    def __init__(self, name):
        self.hot_dog = HotDog(name)  # "Базовый" ход-дог
        self.sauce = SauceIngredient()  # Фабрика соусов
        self.topping = ToppingIngredient()  # Фабрика топпингов

    def add_sauce(self, sauce: str) -> None:
        """
        Добавляет соус
        """
        sauce = self.sauce.create_ingredient(sauce)
        self.hot_dog.add_ingredient(sauce)

    def add_topping(self, topping: str) -> None:
        """
        Добавляет топпинг
        """
        topping = self.topping.create_ingredient(topping)
        self.hot_dog.add_ingredient(topping)


class ClassicBuilder(HotDogBuilder):
    """
    Строитель 'классического' хот-дога
    """

    def __init__(self, name='классический'):
        super().__init__(name)

    def make_hot_dog(self, sauce1='майонез', sauce2='кетчуп', sauce3='горчица') -> HotDog:
        self.add_sauce(sauce1)
        self.add_sauce(sauce2)
        self.add_sauce(sauce3)
        return self.hot_dog


class SweetOnionBuilder(HotDogBuilder):
    """
    Строитель хот-дога со сладким луком
    """

    def __init__(self, name='сладкий лук'):
        super().__init__(name)

    def make_hot_dog(self, sauce='кетчуп', topping='лук') -> HotDog:
        self.add_sauce(sauce)
        self.add_topping(topping)
        return self.hot_dog


class HotPepperBuilder(HotDogBuilder):
    """
    Строитель хот-дога с острым перцем
    """

    def __init__(self, name='острый перец'):
        super().__init__(name)

    def make_hot_dog(self, sauce1='майонез', sauce2='кетчуп', sauce3='горчица',
                     topping1='халапеньо', topping2='чили') -> HotDog:
        self.add_sauce(sauce1)
        self.add_sauce(sauce2)
        self.add_sauce(sauce3)
        self.add_topping(topping1)
        self.add_topping(topping2)
        return self.hot_dog


class IndividualBuilder(HotDogBuilder):
    """
    Строитель индивидуальной пиццы
    """

    def __init__(self, name='индивидуальный'):
        super().__init__(name)

    def make_hot_dog(self, sauces=None, toppings=None) -> HotDog:
        # Принимает списки ингредиентов
        for sauce in sauces:
            self.add_sauce(sauce)
        for topping in toppings:
            self.add_topping(topping)
        return self.hot_dog


class Cook:
    """
    Директор, который управляет строителями хот-догов
    """

    def __init__(self):
        self.builder = None

    def set_builder(self, builder: HotDogBuilder) -> None:
        self.builder = builder

    def make_hot_dog(self, hot_dog: str) -> HotDog:
        if hot_dog == 'классический':
            self.set_builder(ClassicBuilder())
            return self.builder.make_hot_dog()
        elif hot_dog == 'сладкий лук':
            self.set_builder(SweetOnionBuilder())
            return self.builder.make_hot_dog()
        elif hot_dog == 'острый перец':
            self.set_builder(HotPepperBuilder())
            return self.builder.make_hot_dog()
        elif hot_dog == 'индивидуальный':
            self.set_builder(IndividualBuilder())

            sauces = []
            number_of_sauces = int(input('Сколько соусов всего? : '))
            print(f'Всего {number_of_sauces} соус(а)')
            for i in range(number_of_sauces):
                sauces.append(input('Какой соус? : '))

            toppings = []
            number_of_toppings = int(input('Сколько добавок всего? : '))
            print(f'Всего {number_of_toppings} добавка(ок)')
            for i in range(number_of_toppings):
                toppings.append(input('Какая добавка? : '))

            return self.builder.make_hot_dog(sauces, toppings)
