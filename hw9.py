
"""
Класс Vehicle (средство передвижения).
У объектов класса Vehicle есть поля:
working_engine - с момента создания равно False,
является обозначением того, заведен двигатель или нет

У объектов класса Vehicle есть методы:
start - выводит надпись "Двигатель заведен",
если working_engine False и меняет его на True

move - выводит надпись "Средство передвижения едет",
если working_engine True

stop - вывод надпись "Двигатель остановлен",
если working_engine True и меняет его на False

У класса Vehicle есть потомки:
Tank - танк
Car - машина
Boat - надувная лодка

Все объекты классов никаких дополнительных параметров на вход не получают,
то есть их классы вызываются с пустыми скобками.
У классов-потомков только один родитель - Vehicle.
"""


class Vehicle:

    working_engine = False

    # в методе start() можно и не использовать оператор ветвления,
    # ограничившись присвоением self.working_engine = True.
    # Однако он присутствует для (вероятно) лучшей 'читабельности'
    # и для более 'плавного' добавления функционала, обусловленного
    # проверкой текущего значения self.working_engine
    def start(self):
        if not self.working_engine:
            self.working_engine = True
            print('Двигатель заведен')

    def move(self):
        if self.working_engine:
            print('Средство передвижения едет')

    def stop(self):
        self.working_engine = False
        print('Двигатель остановлен')


"""
У объектов класса Tank есть поля:
count_ammo - с момента создания равно 10, боезапас танка

У объектов класса Tank есть методы:
move - выводит надпись "Гусиницы заскрипели от движения",
если working_engine True, иначе выдаёт надпись "Нужно завести двигатель"

shoot - выводит надпись "Танк выстрелил" и уменьшает count_ammo на 1,
если count_ammo > 0, иначе выдаёт надпись "Снаряды кончились"
"""


class Tank(Vehicle):

    count_ammo = 10

    def move(self):
        if self.working_engine:
            print('Гусиницы заскрипели от движения')
        else:
            print('Нужно завести двигатель')

    def shoot(self):
        if self.count_ammo > 0:
            self.count_ammo -= 1
            print('Танк выстрелил')
        else:
            print('Снаряды кончились')


"""
У объектов класса Car есть поля:
fuel - с момента создания равно 100, топливо машины

У объектов класса Car есть методы:
start - выводит надпись "Двигатель машины заведён",
если working_engine False, и меняет его на True. 
Если fuel <= 0, выдаёт надпись "Бензина нет"

move - выводит надпись "Машина поехала" и уменьшает fuel на 10,
если working_engine True, иначе выдаёт надпись "Машина не заведена",
если fuel во время езды станет <= 0, тогда вывести надпись "Машина заглохла"
и установить working_engine на False
"""


class Car(Vehicle):

    fuel = 100

    def start(self):
        if (not self.working_engine) and (self.fuel > 0):
            self.working_engine = True
            print('Двигатель машины заведён')
        elif self.fuel <= 0:
            print('Бензина нет')

    def move(self):
        if not self.working_engine:
            print('Машина не заведена')
        elif self.working_engine and (self.fuel >= 10):
            self.fuel -= 10
            print('Машина поехала')
        elif self.working_engine and (self.fuel <= 0):
            self.working_engine = False
            print('Машина заглохла')


"""
У объектов класса Boat есть поля:
air_pressure - с момента создания равно 100, давление воздуха внутри лодки

У объектов класса Boat есть методы:
start - выводит надпись "Мотор лодки гудит", если working_engine False,
и меняет его на True. Если если air_pressure <= 0, выдаёт надпись "Лодка тонет!"
и двигатель не заводится

move - выводит надпись "Лодка плывёт", если working_engine True,
и уменьшает air_pressure на 10, иначе выдаёт надпись "Мотор лодки не заведен"
"""


class Boat(Vehicle):

    air_pressure = 100

    def start(self):
        if (not self.working_engine) and (self.air_pressure > 0):
            self.working_engine = True
            print('Мотор лодки гудит')
        elif self.air_pressure <= 0:
            print('Лодка тонет!')

    def move(self):
        if self.working_engine:
            self.air_pressure -= 10
            print('Лодка плывёт')
        else:
            print('Мотор лодки не заведен')


def main():
    v = Vehicle()
    t = Tank()
    c = Car()
    b = Boat()

    print('\n')
    print('- Vehicle test -')
    v.move()
    v.start()
    v.move()
    v.move()
    v.stop()
    print('\n')

    print('- Tank test -')
    t.move()
    t.start()
    t.move()
    for i in range(1, 12):
        t.shoot()
    t.stop()
    print('\n')

    print('- Car test -')
    c.move()
    c.start()
    for i in range(1, 12):
        c.move()
    c.start()
    print('\n')

    print('- Boat test -')
    b.move()
    b.start()
    for i in range(1, 7):
        b.move()
    b.stop()
    b.start()
    for i in range(1, 5):
        b.move()
    b.stop()
    b.start()
    print('\n')


if __name__ == '__main__':
    main()
