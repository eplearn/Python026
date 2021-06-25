from core.fast_food_restaurant import RestaurantFacade
from core.client import Client


def main():

    restaurant = RestaurantFacade()
    client1 = Client('Тинки-Винки', 2000)
    client2 = Client('Дипси', 1500)
    client3 = Client('Ляля', 750)
    client4 = Client('По', 600)
    client5 = Client('Пылесос', 150)

    print(f'\nThere are ingredients: {restaurant.available_ingredients.get_data()} you can chose.\n')

    print('"индивидуальный"')
    hot_dog1 = restaurant.make_order(client1, 'индивидуальный')
    print(f'\n{client1.get_name()} -> {hot_dog1}\n')

    print('"острый перец"')
    hot_dog2 = restaurant.make_order(client2, 'острый перец')
    print(f'\n{client2.get_name()} -> {hot_dog2}\n')

    print('"сладкий лук"')
    hot_dog3 = restaurant.make_order(client3, 'сладкий лук')
    print(f'\n{client3.get_name()} -> {hot_dog3}\n')

    print('"классический"')
    hot_dog4 = restaurant.make_order(client4, 'классический')
    print(f'\n{client4.get_name()} -> {hot_dog4}\n')

    print('"индивидуальный"')
    hot_dog5 = restaurant.make_order(client5, 'индивидуальный')
    print(f'\n{client5.get_name()} -> {hot_dog5}\n')


if __name__ == '__main__':
    main()
