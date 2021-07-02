import random as rand
import math
import re
import pathlib
from pathlib import Path
import threading


def main():
    path = input_path()

    lock = threading.Lock()

    filling_thread = threading.Thread(target=random_fill, args=(path, lock))
    primes_thread = threading.Thread(target=calc_primes, args=(path,))
    factorials_thread = threading.Thread(target=calc_factorials, args=(path,))

    filling_thread.start()
    primes_thread.start()
    factorials_thread.start()

    filling_thread.join()
    primes_thread.join()
    factorials_thread.join()


def input_path():
    line = input('enter path to file: ')
    path = Path(line)
    return path


def random_fill(path, lock):
    with lock:
        data_length = 100
        data = []
        for i in range(data_length):
            data.append(rand.randint(1, 1000))

        with path.open(mode='w') as file:
            file.write(str(data))


def find_numbers(path):
    numbers = []
    with path.open(mode='r') as file:
        for line in file:
            nums = re.findall(r'\d+', line.strip('\n'))
            numbers.extend(nums)
    return list(map(int, numbers))


def find_primes(numbers):
    primes = []
    for number in numbers:
        if check_prime(number):
            primes.append(number)
    return primes


def check_prime(number):
    if number > 1:
        for i in range(2, int(number / 2) + 1):
            if (number % i) == 0:
                return False
        else:
            return True
    else:
        return False


def calc_primes(path):
    print(f'numbers {find_numbers(path)}')
    primes = find_primes(find_numbers(path))
    print(f'primes {primes}')
    with open('primes.txt', 'w') as f:
        f.write(str(primes))


def calc_factorials(path):
    print(f'numbers {find_numbers(path)}')
    numbers = find_numbers(path)
    factorials = []
    for number in numbers:
        factorials.append(math.factorial(number))
    print(f'factorials {factorials}')
    with open('factorials.txt', 'w') as f:
        f.write(str(factorials))


if __name__ == '__main__':
    main()
