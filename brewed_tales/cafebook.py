from book import Book

class CafeBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.__price = price

    @property
    def price(self):
        return self.__price

    def display_info(self):
        return f"Café Book: {self.title} by {self.author}, Price: ${self.price}"

    @staticmethod
    def book_type():
        return "This is a café book."
