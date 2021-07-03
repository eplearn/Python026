import concurrent
from concurrent.futures import ThreadPoolExecutor
import threading
import random as rand
import time


def random_fill(data, data_length, lock):
    with lock:
        print('\nrandom_fill is started')
        for i in range(data_length):
            data.append(rand.randint(1, 1000))
        print('\nrandom_fill is stopped')


def calc_sum(data, answer):
    print('\ncalc_sum is started')
    answer[0] = sum(data)


def calc_mean(data, answer):
    print('\ncalc_mean is started')
    answer[1] = (sum(data)) / len(data)


def main():
    # number of elements
    data_length = 100000
    data = []
    # answer[0] = sum, answer[1] = mean
    answer = [0, 0]

    start_time = time.time()
    lock = threading.Lock()

    # следует сделать так, чтобы передавалось возвращаемое значение одного потока в качестве аргумента функции другого
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(random_fill, data, data_length, lock=lock)
        executor.submit(calc_sum, data, answer)
        executor.submit(calc_mean, data, answer)

    # print(f' data list is: {data}\n\nsum is: {answer[0]}\n\nmean is: {answer[1]}\n\n')
    print('\n***************\n')
    print(f'\nВремя исполнения: {time.time() - start_time} сек\n')
    print(f'Reult: \nsum = {answer[0]}, mean = {answer[1]}')

    print(f'Verifying: \nsum = {sum(data)}, mean = {sum(data)/len(data)}')


if __name__ == '__main__':
    main()
