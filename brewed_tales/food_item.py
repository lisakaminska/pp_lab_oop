class FoodItem:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    def display_info(self):
        return f"Food Item: {self.name}, Price: ${self.price}"

    @staticmethod
    def food_type():
        return "This is a food item."
