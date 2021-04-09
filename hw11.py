
"""
Реализовать иерархию классов согласно приложенной UML-даиграмме.

Есть общий класс Person, от которого наследуются классы Terrorist
и CounterTerrorist.
Есть класс Gun, от которого наследуются AK и M4,
каждый из которых состоит в отношении агрегации
соответственно игровой роли (АК для террористов, М4 для контер-террористов).

Реализации стрельбы и перезарядки для каждого класса остаются на усмотрение
разработчика. При желании что-то можно добавить.
"""

"""
Классы M4 и AK содержат переменные magazine и num_of_magazines,
которые определяют количество боеприпасов экземпляров соответствующих классов.

Экземпляры указанных выше классов содержат свойство is_magazine_empty,
являющееся маркером опустошения магазина.
Оно используется для формирования поведения, реализуемого методами reload():
перезараядка требуется при условии опустошения магазина.
А также is_magazine_empty используется при тестировании.
"""


class Gun:
    def __init__(self, ammo):
        self.ammo = ammo

    def shoot(self):
        if self.ammo > 0:
            self.ammo -= 1
            print('gun is shooting!')
        else:
            print("Can't shoot - out of ammo!")

    def reload(self):
        if self.ammo > 0:
            print('gun is reloading!')
        else:
            print("Can't reload - out of ammo!")


class M4(Gun):
    magazine = 20
    num_of_magazines = 2

    def __init__(self):
        super().__init__(M4.magazine * M4.num_of_magazines)
        self.is_magazine_empty = False

    def shoot(self):
        if self.ammo == 0:
            print("M4 can't shoot - out of ammo!")
        elif self.ammo > 0 and not self.is_magazine_empty:
            if self.ammo % M4.magazine == 1:
                self.is_magazine_empty = True
            self.ammo -= 1
            print('M4 is shooting!')
        elif self.ammo > 0 and self.is_magazine_empty:
            print("M4 can't shoot, magazine is empty, reload the gun!")

    def reload(self):
        if self.ammo > 0:
            if not self.is_magazine_empty:
                self.ammo -= self.ammo % M4.magazine
            print('----------------------- M4 is reloading!')
            self.is_magazine_empty = False
        else:
            print("----------------------- M4 can't reload - out of ammo!")


class AK(Gun):
    magazine = 30
    num_of_magazines = 2

    def __init__(self):
        super().__init__(AK.magazine * AK.num_of_magazines)
        self.is_magazine_empty = False

    def shoot(self):
        if self.ammo == 0:
            print("AK can't shoot - out of ammo!")
        elif self.ammo > 0 and not self.is_magazine_empty:
            if self.ammo % AK.magazine == 1:
                self.is_magazine_empty = True
            self.ammo -= 1
            print('AK is shooting!')
        elif self.ammo > 0 and self.is_magazine_empty:
            print("AK can't shoot, magazine is empty, reload the gun!")

    def reload(self):
        if self.ammo > 0:
            if not self.is_magazine_empty:
                self.ammo -= self.ammo % AK.magazine
            print('----------------------- AK is reloading!')
            self.is_magazine_empty = False
        else:
            print("----------------------- AK can't reload - out of ammo!")


class Person:
    def __init__(self):
        self.health = 100

    def shoot(self):
        print('Alert! Someone is shooting!')

    def reload(self):
        print('Alert! Someone is reloading!')


class Terrorist(Person):
    def __init__(self):
        super().__init__()
        self.gun = AK()

    def shoot(self):
        self.gun.shoot()

    def reload(self):
        self.gun.reload()


class CounterTerrorist(Person):
    def __init__(self):
        super().__init__()
        self.gun = M4()

    def shoot(self):
        self.gun.shoot()

    def reload(self):
        self.gun.reload()


def main():
    # p = Person()
    # print(p.health)
    # print(p.shoot)
    # print(p.reload)
    #
    # m4 = M4()
    # print(m4.shoot())
    # print(m4.reload())
    #
    # ak74 = AK()
    # print(ak74.shoot())
    # print(ak74.reload())

    terr = Terrorist()
    counter = CounterTerrorist()

    for i in range(1, 62):
        print('........................\n')
        print(i)
        counter.shoot()
        print(f"M4's is_magazine_empty: {counter.gun.is_magazine_empty}")
        if counter.gun.is_magazine_empty:
            counter.reload()
        print('')
        terr.shoot()
        print(f"AK's is_magazine_empty: {terr.gun.is_magazine_empty}")
        if terr.gun.is_magazine_empty:
            terr.reload()


if __name__ == '__main__':
    main()
