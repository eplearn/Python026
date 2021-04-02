import random


"""
Создать класс Дробное число со знаком (Fractions). Число должно быть представлено
двумя полями: целая часть - длинное целое со знаком, дробная часть - беззнаковое
короткое целое. Реализовать арифметические операции сложения, вычитания, умножения
и операции сравнения.
"""


class FractionNum:
    def __init__(self, whole, frac):
        self.whole = int(whole)
        # по условию следует хранить int,
        # поэтому добавляем один старший разряд и задаем ему значение '1'
        self.fraction = int(f'1{frac}')

    def __str__(self):
        return str(self.whole) + '.' + str(self.fraction)[1::]

    def __add__(self, other):
        result_whole = self.whole + other.whole

        first = self.fraction
        second = other.fraction

        diff_len = abs(len(str(self.fraction)) - len(str(other.fraction)))
        if len(str(self.fraction)) > len(str(other.fraction)):
            second = int(str(other.fraction) + '0' * diff_len)
        else:
            first = int(str(self.fraction) + '0' * diff_len)

        tmp_frac = first + second

        result_fraction = str(tmp_frac)[1::]
        if int(str(tmp_frac)[0]) > 2:
            result_whole += 1

        return FractionNum(result_whole, result_fraction)


def main():
    for i in range(25):
        r1 = random.uniform(0, 10)
        f1 = str(r1 % 1)[2::4]
        a = FractionNum(int(r1), f1)
        k1 = int('1'+'0'*len(f1))

        r2 = random.uniform(0, 10)
        f2 = str(r2 % 1)[2::4]
        b = FractionNum(int(r2), f2)
        k2 = int('1'+'0'*len(f2))

        answer = round((int(r1) + (float(f1) / k1)) + (int(r2) + (float(f2) / k2)), 5)

        print(f'a = {a}, b = {b}, a + b = {a + b}     | answer is   {answer}')

    # a = FractionNum(10, '08')
    # b = FractionNum(10, '08')
    # c = a + b
    # print(f'\nc = a + b = {a} + {b} = {c}')


if __name__ == '__main__':
    main()
