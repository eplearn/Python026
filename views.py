class UserInterface:
    def wait_user_response(self):
        print('\n' + ' Input data '.center(30, '*'))
        print('What shall be done, Master?\n')
        user_response = input("Chose actions from below, please: "
                              "\n add a recipe (enter '1');"
                              "\n look at recipe (enter '2');"
                              "\n look at all of recipes (enter '3');"
                              "\n delete a recipe (enter '4')."
                              "\n quit (enter 'q')"
                              "\n" + '*'.center(30, '*') + '\n')
        return user_response

    def enter_recipe_name(self):
        recipe_name = input("Enter the recipe name, please.\n")
        return recipe_name

    def enter_recipe(self):
        recipe_list = []
        ingredients = set()
        number_of_ingredients = 0

        while number_of_ingredients == 0:
            print('Enter number of ingredients, please.\n')
            number_of_ingredients = input()
        for i in range(int(number_of_ingredients)):
            ingredients.add(input('Enter name of the ingredient, please.\n'))

        recipe_list.append(str(input("Enter the recipe name, please.\n")))
        recipe_list.append(input("Enter the author name, please.\n"))
        recipe_list.append(input("Enter the course name, please.\n"))
        recipe_list.append(input("Enter the description of recipe, please.\n"))
        recipe_list.append(ingredients)
        recipe_list.append(input("Enter the cuisine name, please.\n"))

        return recipe_list

    def show_recipe(self, recipe):
        print(str(recipe))

    def show_all_recipes(self, all_recipes):
        print(str(all_recipes))
