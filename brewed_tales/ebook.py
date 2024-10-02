from book import Book

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.__file_size = file_size

    @property
    def file_size(self):
        return self.__file_size

    def display_info(self):
        return f"E-Book: {self.title} by {self.author}, File Size: {self.file_size}MB"

    @staticmethod
    def book_type():
        return "This is an e-book."
