

class UserInterface:
    def wait_user_response(self):
        print(' Input data '.center(30, '*'))
        print('What shall be done done, Master?')
        user_response = input('Chose actions, please: '
                              '\n add a recipe;'
                              '\n look at recipe;'
                              '\n look at all of recipes;'
                              '\n delete a recipe.')
        return user_response
