from model import DataStorage, Recipe
from views import UserInterface


class Controller:
    def __init__(self):
        self.data = DataStorage()
        self.user_interface = UserInterface()
        self.user_responses = []

    def add_recipe(self):
        recipe_list = self.user_interface.enter_recipe()
        recipe = Recipe(recipe_list[0], recipe_list[1], recipe_list[2], recipe_list[3], recipe_list[4],
                        recipe_list[5])
        self.data.add_recipe(recipe)

    def get_recipe(self, recipe_name):
        recipe = self.data.get_recipe(recipe_name)
        self.user_interface.show_recipe(recipe)

    def get_all_recipes(self):
        all_recipes = self.data.get_all_recipes()
        self.user_interface.show_all_recipes(all_recipes)

    def delete_recipe(self, recipe_name):
        self.data.delete_recipe(recipe_name)

    def handle_user_response(self, response):
        if response == '1':
            self.add_recipe()
        elif response == '2':
            recipe_name = self.user_interface.enter_recipe_name()
            self.get_recipe(recipe_name)
        elif response == '3':
            self.get_all_recipes()
        elif response == '4':
            recipe_name = self.user_interface.enter_recipe_name()
            self.delete_recipe(recipe_name)

    def run(self):
        response = None
        while response != 'q':
            response = self.user_interface.wait_user_response()
            self.handle_user_response(response)
