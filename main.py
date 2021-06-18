from model import DataStorage, Recipe


def main():
    db = DataStorage('First base')
    db.init_recipes()
    print(str(db))
    print('\n')
    print(str(db.get_recipe('recipe_name_7')))
    print('\n')
    print(str(db.get_recipe('recipe_name_10')))
    print('\n')
    db.delete_recipe('recipe_name_10')
    print(str(db))
    print(str(db.get_recipe('recipe_name_10')))
    print('\n')
    print(str(db.get_all_recipes()))
    print('\n')


if __name__ == '__main__':
    main()
