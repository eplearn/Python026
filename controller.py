from model import DataStorage, Recipe
from views import UserInterface


class Controller:
    def __init__(self):
        self.data = DataStorage()
        self.user_interface = UserInterface()
