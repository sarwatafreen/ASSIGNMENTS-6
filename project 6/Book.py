# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.
class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_books += 1

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def get_total_books(cls):
        return cls.total_books

    def __str__(self):
        return f"Book: {self.title}, Author: {self.author}"
book1 = Book("1984", "George Orwell")
book2 = Book("Animal Farm", "George Orwell")

print(book1)
print("Total books:", Book.get_total_books())


#