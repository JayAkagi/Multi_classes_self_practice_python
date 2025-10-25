from library import *
from book import *

book1 = Book("Title1", "Author1")
book2 = Book("Title2", "Author2")
book3 = Book("Title3", "Author3")
book4 = "Title5, Author5"

city_library = Library()

city_library.add_book(book1)
city_library.add_book(book2)
city_library.add_book(book3)
city_library.add_book(book4)

for book in city_library.get_all_books():
    print(book.description())