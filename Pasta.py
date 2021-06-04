class Pasta:

    def __init__(self, name):
        # Наименование блюда.
        self.name = name
        # Перечень входящих ингредиентов.
        self.ingredients = []

    def set_pasta(self, pasta):
        self.ingredients.append(pasta)

    def set_sauce(self, sause):
        self.ingredients.append(sause)

    def set_filling(self, filling):
        self.ingredients.append(filling)

    def set_additive(self, additive):
        self.ingredients.append(additive)

    def __str__(self):
        return 'Pasta name is ' + str(self.name) + ', ingredients are: ' + str(self.ingredients) + '.'
