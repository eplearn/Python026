from book import Book
from librarian import Librarian
from reader import Reader


class Library:

    def __init__(self, name, books_quantity, librarians_quantity):

        self.name = name
        self.books_quantity = books_quantity
        self.librarians_quantity = librarians_quantity
        self.books = []
        self.librarians = []

        for i in range(librarians_quantity):
            librarian = Librarian()
            self.librarians.append(librarian)

        for i in range(books_quantity):
            book = Book()
            self.books.append(book)
            for librarian in self.librarians:
                librarian.add_book(book)

        print(f"Library '{self.name}' is created.")

    def __str__(self):
        return f"Library name is {self.name}. It has books: {self.books}. List of librarians is {self.librarians}."

    def get_book(self, book_name, reader):
        reader.grab_book(self.librarians[0].give_book(book_name, reader.name), self.librarians[0].name)

    def return_book(self, book_name, reader):
        self.librarians[0].add_book(reader.return_book(book_name))
