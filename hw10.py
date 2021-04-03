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
        result_fraction = 0

        first = self.fraction
        second = other.fraction

        diff_len = abs(len(str(self.fraction)) - len(str(other.fraction)))
        if len(str(self.fraction)) > len(str(other.fraction)):
            second = int(str(other.fraction) + '0' * diff_len)
        else:
            first = int(str(self.fraction) + '0' * diff_len)

        if (self.whole > 0 and other.whole > 0) or (self.whole < 0 and other.whole < 0):
            tmp_frac = first + second
            result_fraction = str(tmp_frac)[1::]
            if int(str(tmp_frac)[0]) > 2:
                if self.whole < 0 and other.whole < 0:
                    result_whole -= 1
                else:
                    result_whole += 1

        elif self.whole > 0 > other.whole:

            if first > second:
                tmp_frac = first - int(str(second)[1::])
                result_fraction = str(int('1' + '0' * len(str(tmp_frac))) - tmp_frac)[1::]
                result_whole += 1

            elif first < second:
                tmp_frac = first - int(str(second)[1::])
                result_fraction = str(tmp_frac)[0::]
                result_whole -= 1

        elif self.whole < 0 < other.whole:

            if first > second:
                tmp_frac = first - int(str(second)[1::])
                result_fraction = str(int('1' + '0' * len(str(tmp_frac))) - tmp_frac)[1::]
                result_whole -= 1

            elif first < second:
                tmp_frac = first - int(str(second)[1::])
                result_fraction = str(int('1' + '0' * (len(str(tmp_frac)) + 1)) - tmp_frac)[1::]

        else:
            tmp_frac = first + second
            print(f'tmp_frac = {tmp_frac}')
            result_fraction = str(tmp_frac)[1::]
            print(f'result_fraction = {result_fraction}')
            if int(str(tmp_frac)[0]) > 2:
                if self.whole < 0 and other.whole < 0:
                    result_whole -= 1
                else:
                    result_whole += 1

        return FractionNum(result_whole, result_fraction)

    def __sub__(self, other):
        # для того, чтобы не влиять на исходный объект, создадим новый
        tmp = FractionNum(-other.whole, str(other.fraction)[1::])
        return self + tmp

    def __mul__(self, other):
        d_places = len(str(self.fraction)) + len(str(other.fraction)) - 2

        first_frac = int(str(self.fraction)[1::]) / int('1' + '0' * (len(str(self.fraction)) - 1))
        second_frac = int(str(other.fraction)[1::]) / int('1' + '0' * (len(str(other.fraction)) - 1))
        first_whole = abs(self.whole)
        second_whole = abs(other.whole)

        index = 2
        coef = 1
        if (self.whole > 0 > other.whole) or (self.whole < 0 < other.whole):
            index = 3
            coef *= -1

        ww = first_whole * second_whole
        wf = first_whole * second_frac
        fw = first_frac * second_whole
        ff = first_frac * second_frac

        sumn = (ww + wf + fw + ff) * coef
        new_whole = int(sumn)
        new_frac = str(sumn - new_whole)[index:index + d_places]

        return FractionNum(new_whole, new_frac)

    def __gt__(self, other):
        if self.whole > other.whole:
            return True
        elif self.whole == other.whole and self.fraction > other.fraction:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.whole == other.whole and self.fraction == other.fraction:
            return True
        else:
            return False


def main():
    print('\n')
    for i in range(5):
        r1 = random.uniform(0, 10)
        f1 = str(r1 % 1)[2::4]
        a = FractionNum(int(r1), f1)
        k1 = int('1' + '0' * len(f1))

        r2 = random.uniform(0, 10)
        f2 = str(r2 % 1)[2::4]
        b = FractionNum(int(r2), f2)
        k2 = int('1' + '0' * len(f2))

        answer = round((int(r1) + (float(f1) / k1)) + (int(r2) + (float(f2) / k2)), 5)

        print(f'a = {a},   b = {b},    a + b = {a + b}        | answer is   {answer}')

    fn1 = FractionNum(-10, '0')
    fn2 = FractionNum(11, '8')
    fn3 = fn1 + fn2
    fn4 = fn1 - fn2
    fn5 = FractionNum(-21, '8')
    fn6 = FractionNum(10, '05')
    fn7 = FractionNum(-4, '2')
    fn8 = fn6 * fn7

    print(f'\nfn1 = {fn1}, fn2 = {fn2}, | fn3 = {fn1} + {fn2} = {fn3}')
    print(f'\nfn1 = {fn1}, fn2 = {fn2}, | fn4 = {fn1} - {fn2} = {fn4}')
    print(f'\nfn4 = {fn4}, fn5 = {fn5}, | fn4 == fn5 is {fn4 == fn5}')
    print(f'\nfn4 = {fn4}, fn5 = {fn5}, | fn4 > fn5 is {fn4 > fn5}')
    print(f'\nfn6 = {fn6}, fn7 = {fn7}, | fn8 = {fn6} * {fn7} = {fn8}')

    # x = FractionNum(0, '29025')
    # y = FractionNum(4, '6679')
    # z = x + y
    # print(f'\nx = {x}, y = {y}, | z = {x} + {y} = {z}')

if __name__ == '__main__':
    main()
