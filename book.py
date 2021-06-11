class Book:
    quantity = 0

    def __init__(self):
        Book.quantity += 1
        self.id_number = Book.quantity
        self.name = 'name' + str(self.id_number)
        self.text = 'text' + str(self.id_number)

    def __str__(self):
        return f"Book name is '{self.name}', text is '{self.text}'."

    def change(self):
        self.name = str(self.name) + ' is censored'
        self.text = str(self.text) + ' is censored'
