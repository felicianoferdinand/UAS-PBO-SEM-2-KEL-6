from library_model import Book, Computer

class Library:
    def __init__(self):
        self.books = [Book("Introduction to Algorithms", "Thomas H. Cormen"), Book("Python Crash Course", "Eric Matthes")]
        self.computers = [Computer("MacBook Pro", "Apple"), Computer("ThinkPad X1 Carbon", "Lenovo")]

    def borrow_book(self, student_name, book_name):
        for book in self.books:
            if book.name == book_name and book.available:
                book.available = False
                return f"{student_name} borrowed the book '{book.name}'"
        return "Sorry, the requested book is not available."

    def borrow_computer(self, user_name, computer_name):
        for computer in self.computers:
            if computer.name == computer_name and computer.available:
                computer.available = False
                return f"{user_name} borrowed the computer '{computer.name}'"
        return "Sorry, the requested computer is not available."

    def view_books(self):
        return [{"name": book.name, "author": book.author, "available": book.available} for book in self.books]

    def view_computers(self):
        return [{"name": computer.name, "brand": computer.brand, "available": computer.available} for computer in self.computers]
