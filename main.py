
import time
from receiver import Receiver


def main():
    start_time = time.time()
    rec = Receiver(500, 'data.txt', 'https://random-data-api.com/api/phone_number/random_phone_number')
    rec.run()
    end_time = time.time()
    print(f'Время: {end_time - start_time} сек.')


if __name__ == '__main__':
    main()

