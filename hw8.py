from collections import Counter
import re


# Задача 1. Найти количество различных элементов массива.
# Пример: для [1 4 5 1 1 3] ответ 4.
def count_unique_elements(arr):
    return len(set(arr))


# Задача 2. Дан файл с логинами и паролями. Найдите топ10 самых популярных паролей.
# Ссылка на файл: https://yadi.sk/i/6ywJqzm93HGmy9
def get_top10_popular_pwd(filename):
    text = []
    with open(filename, 'r', encoding='utf-8') as reader:
        for line in enumerate(reader):
            text.append(re.findall(r'[^;,\n]+', reader.readline())[1])
    return [key for key, _ in Counter(text).most_common(10)]


# Задача 3. Дана строка с ссылками. Заменить все ссылки на ***** (5 звёздочек).
# Примеры ссылок:
# www.site.com заменится на *****
# http://example.su заменится на *****
# vk.ru заменится на *****
# и т.д.
# Чем больше разных вариантов будет придумано, тем лучше, но без фанатизма.
# Для простоты, ограничьте набор доменов верхнего уровня (штуки 4-7 достаточно).
def censor_link(string):
    # Паттерн для замены ссылок в строке будем составлять "на ходу".
    answer = ''
    prefix = ['http:\/\/', 'https:\/\/', 'http:\/\/www', 'https:\/\/www', 'www', '']
    postfix = ['com', 'su', 'ru', 'net', 'org']
    sub_pattern = ''
    pattern = ''
    for pre in prefix:
        for post in postfix:
            sub_pattern = f'({pre}.\w+.{post})'
            if pattern == '':
                pattern = sub_pattern
            else:
                pattern = pattern + '|' + sub_pattern
    answer = re.sub(f'{pattern}', ' ***** ', string)
    # Исключим из возвращаемой строки лишние пробелы.
    return re.sub(r'\s+', ' ', answer)


def main():
    # task 1
    print(f'\n Task 1:')
    data_task_1 = [[1, 4, 5, 1, 1, 3], [1, 0, 7, 1, 1, 7], ['1', 4, 5, 'a', 1, 3]]
    for arr in data_task_1:
        print(f' Array {arr} has {count_unique_elements(arr)} unique elements.')

    # task 2
    print(f'\n Task 2:')
    print(*get_top10_popular_pwd('pwd.txt'))

    # task 3
    print(f'\n Task 3:')
    data_task_3 = 'Faina www.site.com http://example.su loves vk.ru ' \
                  'https://www.python.org pikachu so cpanel.net much.'
    print(f'Uncensored string is {data_task_3}')
    print(f'  Censored string is {censor_link(data_task_3)}')


if __name__ == '__main__':
    main()
