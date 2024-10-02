class DigitalItem:
    def __init__(self, file_size):
        self.__file_size = file_size

    @property
    def file_size(self):
        return self.__file_size

    def digital_info(self):
        return f"File Size: {self.file_size}MB"
