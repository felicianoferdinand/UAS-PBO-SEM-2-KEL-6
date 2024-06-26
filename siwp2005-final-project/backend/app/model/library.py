class LibraryItem:
    def __init__(self, name):
        self.name = name
        self.available = True

class Book(LibraryItem):
    def __init__(self, name, author):
        super().__init__(name)
        self.author = author

class Computer(LibraryItem):
    def __init__(self, name, brand):
        super().__init__(name)
        self.brand = brand
