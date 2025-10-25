class Book():
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def description(self):
        return f"{self.title} by {self.author}"