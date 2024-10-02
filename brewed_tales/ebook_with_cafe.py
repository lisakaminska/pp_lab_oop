from book import Book
from digital_item import DigitalItem

class EBookWithCafe(Book, DigitalItem):
    def __init__(self, title, author, file_size, price):
        Book.__init__(self, title, author)
        DigitalItem.__init__(self, file_size)
        self.__price = price

    @property
    def price(self):
        return self.__price

    def display_info(self):
        return f"E-Book with Café: {self.title} by {self.author}, File Size: {self.file_size}MB, Price: ${self.price}"

    @staticmethod
    def book_type():
        return "This is an e-book with café."
