import random as rand


class DataStorage:
    def __init__(self, name='storage'):
        self.name = name
        self.recipes = {}
        self.clients = {}
        self.init_recipes()

    def __str__(self):
        return f"Data storage's name is {self.name}, recipes are: {str(self.recipes)}, clients are: {self.clients}"

    def init_recipes(self):
        for i in range(0, 10):
            Recipe.add_ingredient(str(i))

        default_recipe_name = 'recipe_name'
        default_author_name = 'author_name'
        default_description = 'description'
        default_course_name = 'course_name'
        default_cuisine_name = 'cuisine_name'

        for i in range(1, 11):
            ingredient_set = set()
            for j in range(5):
                ingredient_set.add(rand.randint(1, Recipe.get_ingredient_number()))
            recipe = Recipe(f'{default_recipe_name}_{i}', f'{default_author_name}_{i}', f'{default_course_name}_{i}',
                            f'{default_description}_{i}', ingredient_set, f'{default_cuisine_name}_{i}')
            self.recipes[recipe.get_recipe_name()] = recipe

    def add_recipe(self, recipe):
        key = recipe.get_recipe_name()
        self.recipes.update({key: recipe})

    def delete_recipe(self, recipe_name):
        recipe = self.recipes.get(recipe_name)
        if recipe is not None:
            del self.recipes[recipe_name]
        else:
            return f"There is no recipe '{recipe_name}' in current data storage."

    def get_recipe(self, recipe_name):
        recipe = self.recipes.get(recipe_name)
        if recipe is not None:
            return '\n' + str(recipe)
        else:
            return f"There is no recipe '{recipe_name}' in current data storage."

    def get_all_recipes(self):
        answer = '-'.center(100, '-') + '\n' 'All recipes: \n\n'
        values = self.recipes.values()
        for recipe in values:
            temp = '\n' + str(recipe)
            answer = answer + temp + '\n\n'
        answer = answer + '-'.center(100, '-')
        return answer


class Recipe:
    ingredients = set()

    def __init__(self, name, author, course, description, ingredients, cuisine):
        self.name = name
        self.author = author
        self.course = course
        self.description = description
        self.ingredients = ingredients
        self.cuisine = cuisine

    def __str__(self):
        return f"Recipe's name is '{self.name}', author is '{self.author}', course is '{self.course}',\n" \
               f" description is: \n'{self.description}',\n ingredients are: '{self.ingredients}',\n" \
               f" cuisine is '{self.cuisine}'"

    def get_recipe_name(self):
        return self.name

    @staticmethod
    def add_ingredient(ingredient):
        Recipe.ingredients.add(ingredient)

    @staticmethod
    def get_ingredient_number():
        return len(Recipe.ingredients)
