from drink import Drink

class Coffee(Drink):
    def __init__(self, name, size, is_iced):
        super().__init__(name, size)
        self.__is_iced = is_iced

    @property
    def is_iced(self):
        return self.__is_iced

    def display_info(self):
        iced_status = "Iced" if self.is_iced else "Hot"
        return f"Coffee: {self.name}, Size: {self.size}, Type: {iced_status}"
