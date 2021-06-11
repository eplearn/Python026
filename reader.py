class Reader:

    def __init__(self, name):
        # Имя читателя.
        self.name = name
        # Словарь выданных ему библиотечных книг.
        self.books = {}
        print(f"Reader '{self.name}' is created.")

    def get_book_names(self):
        return list(self.books.keys())

    def grab_book(self, book, librarian_name):
        self.books[book.name] = book
        print(f"{self.name} has grabbed the book '{book.name}' from {librarian_name}.")

    def read_books(self):
        for book_name in self.books:
            # print(str(self.name) + ' is reading the ' + "'" + str(book_name) + "'")
            print(f"{self.name} is reading the book '{book_name}'.")

    def return_book(self, book_name):
        print(f'{self.name} returned the book {book_name}')
        return self.books.pop(book_name)
