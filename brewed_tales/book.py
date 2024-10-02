class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    def display_info(self):
        return f"Book: {self.title} by {self.author}"

    @staticmethod
    def book_type():
        return "This is a book."
