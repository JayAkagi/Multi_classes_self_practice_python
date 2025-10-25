from book import *
from colorama import Fore, Style
class Library():
    def __init__(self):
        self.books: list[Book] = []

    def add_book(self, book: Book):
        if not isinstance(book, Book):
            message = f"{Fore.RED}Exception: Only Book instances can be added{Style.RESET_ALL}"
            print(message)
            return
        self.books.append(book)

    def get_all_books(self):
        return self.books