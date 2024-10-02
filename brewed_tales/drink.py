class Drink:
    def __init__(self, name, size):
        self.__name = name
        self.__size = size

    @property
    def name(self):
        return self.__name

    @property
    def size(self):
        return self.__size

    def display_info(self):
        return f"Drink: {self.name}, Size: {self.size}"

    @staticmethod
    def drink_type():
        return "This is a beverage."
