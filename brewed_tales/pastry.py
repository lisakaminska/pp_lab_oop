from food_item import FoodItem

class Pastry(FoodItem):
    def __init__(self, name, price, is_sweet):
        super().__init__(name, price)
        self.__is_sweet = is_sweet

    @property
    def is_sweet(self):
        return self.__is_sweet

    def display_info(self):
        sweetness_status = "Sweet" if self.is_sweet else "Savory"
        return f"Pastry: {self.name}, Price: ${self.price}, Type: {sweetness_status}"
