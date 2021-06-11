from book import Book


class Librarian:
    quantity = 0

    def __init__(self):
        Librarian.quantity += 1
        self.id_number = Librarian.quantity
        self.name = 'Eratosthenes' + str(self.id_number)

        # Словарь имеющихся в распоряжении книг. Ключ - наименование книги, значение - книга.
        self.books = {}
        # Словарь читателей, которым выданы книги. Ключ - имя читателя, значение - список наименований книг.
        self.readers = {}

    def __str__(self):
        string = f"Librarian {self.name}, has books: {self.books} and serves readers: {self.readers}."
        return string

    def get_book_names(self):
        return list(self.books.keys())

    def add_book(self, book):
        # Добавляет книгу и вычеркивает ее название из списка книг, выданных читателю

        self.books[book.name] = book
        for elem in self.readers.items():
            for book_name in elem[1]:
                if book_name == book.name:
                    elem[1].remove(book_name)
                    print(f"The book '{book.name}' was returned to {self.name}'s collection of books.")
                else:
                    print(f"The book '{book.name}' was added to {self.name}'s collection of books.")

    def give_book(self, book_name, reader_name):
        # Выдаваемая книга фиксируется списке книг, находящихся в распоряжении читателя.
        # Если запрашиваемой книги нет, то добрый сотрудник библиотеки дает почитать свою личную книгу.

        if book_name in self.books.keys():

            if reader_name not in list(self.readers.keys()):
                book_names = [book_name]
                self.readers[reader_name] = book_names
            else:
                self.readers.get(reader_name).append(book_name)

            print(f'The book {book_name} is given to {reader_name} by {self.name}.')
            return self.books.pop(book_name)

        else:
            print(f"'There is no such book here. You may book of mine.' - said librarian {self.name}. And gave it.")
            return Book()

    def change_book(self, name):
        # При наличии книги изменяет ее.

        book = self.books.get(name)
        if book is not None:
            book.change()
            print(f'The book {name} is changed. Whatever that means.')
            temp = book
            self.books.pop(name)
            self.books[book.name] = temp
