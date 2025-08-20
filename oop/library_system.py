class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, file_size, title, author):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"{self.title} by {self.author} (E-book, {self.file_size} KB)"

class PrintBook(Book):
    def __init__(self, page_count, title, author):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"{self.title} by {self.author} (Print book, {self.page_count} pages)"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Only instances of Book or its subclasses can be added to the library.")

    def list_books(self):
        for book in self.books:
            print(book)

