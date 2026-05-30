# Library Management System
# Demonstrates inheritance, super(), and method overriding.

class LibraryItem:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def describe(self):
        return f"{self.title} by {self.author} ({self.year})"


class Book(LibraryItem):
    def __init__(self, title, author, year, pages):
        super().__init__(title, author, year)
        self.pages = pages

    def describe(self):
        return (
            f"Book: {self.title} | "
            f"Author: {self.author} | "
            f"Pages: {self.pages}"
        )


class EBook(LibraryItem):
    def __init__(self, title, author, year, file_size_mb):
        super().__init__(title, author, year)
        self.file_size_mb = file_size_mb

    def describe(self):
        return (
            f"EBook: {self.title} | "
            f"Author: {self.author} | "
            f"Size: {self.file_size_mb} MB"
        )


book1 = Book("Python Basics", "John", 2020, 350)
book2 = Book("Machine Learning", "Andrew", 2021, 500)

ebook1 = EBook("AI Guide", "Sam", 2022, 15)
ebook2 = EBook("Deep Learning", "Max", 2023, 20)

items = [book1, book2, ebook1, ebook2]

for item in items:
    print(item.describe())

# Explore
print(isinstance(book1, LibraryItem))
# True because Book inherits from LibraryItem.