import threading
import random as rand
import time


# global variables (if we have to use them):
# answer_sum = 0
# answer_mean = 0


def random_fill(data, data_length, lock):
    with lock:
        print('\nrandom_fill is started\n')
        for i in range(data_length):
            data.append(rand.randint(1, 1000))
        print('\nrandom_fill is stopped\n')


def calc_sum(data, answer):
    print('\ncalc_sum is started\n')
    answer[0] = sum(data)
    print('\ncalc_sum is stopped\n')
    # if we have to use global variables then:
    # global answer_sum
    # answer_sum = sum(data)


def calc_mean(data, answer):
    print('\ncalc_mean is started\n')
    answer[1] = (sum(data)) / len(data)
    print('\ncalc_mean is stopped\n')
    # if we have to use global variables then:
    # global answer_mean
    # answer_mean = (sum(data)) / len(data)


def main():
    # number of elements
    data_length = 1000000
    data = []
    # answer[0] = sum, answer[1] = mean
    answer = [0, 0]

    start_time = time.time()

    lock = threading.Lock()

    filling_thread = threading.Thread(target=random_fill, args=(data, data_length, lock))
    calc_sum_thread = threading.Thread(target=calc_sum, args=(data, answer))
    calc_mean_thread = threading.Thread(target=calc_mean, args=(data, answer))

    filling_thread.start()
    filling_thread.join()

    calc_sum_thread.start()
    calc_mean_thread.start()

    calc_sum_thread.join()
    calc_mean_thread.join()

    # print(f' data list is: {data}\n\nsum is: {answer[0]}\n\nmean is: {answer[1]}\n\n')
    print(f'\n\nsum is: {answer[0]}\n\nmean is: {answer[1]}\n\n')
    print(f'Время исполнения: {time.time() - start_time} сек')

    # if we have to use global variables then:
    # print(f'global sum = {answer_sum}, global mean = {answer_mean}')

    # print(f'sum = {sum(data)}, mean = {sum(data)/len(data)}')


if __name__ == '__main__':
    main()
