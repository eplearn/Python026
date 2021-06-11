from library import Library
from reader import Reader


def main():

    print('\n')
    library = Library('Roswell', 5, 1)
    reader1 = Reader('Dixie')
    print('\n')

    library.get_book('name1', reader1)
    print('\n')

    reader1.read_books()
    print('\n')

    library.return_book(reader1.get_book_names()[0], reader1)


if __name__ == '__main__':
    main()
