class Library():
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_all_books(self):
        return self.books