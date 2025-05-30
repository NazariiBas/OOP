
class Author:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def get_info(self):
        return f"Ім'я: {self.name}, Рік народження: {self.birth_year}"


class Book:
    def __init__(self, title, author, year, annotation=""):
        self.title = title
        self.author = author  # Це об'єкт класу Author
        self.year = year
        self.annotation = annotation

    def get_info(self):
        info = f"Назва: {self.title}, Рік видання: {self.year}, Автор: {self.author.name}"
        if self.annotation:
            info += f"\n{self.annotation}"
        return info


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []  # список об'єктів Book

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [book.get_info() for book in self.books]

    def find_books_by_author(self, author_name):
        return [book.get_info() for book in self.books if book.author.name == author_name]


# === Створення об'єктів та перевірка ===

# Автори (агрегація — автори існують окремо)
author1 = Author("Ліна Костенко", 1930)
author2 = Author("Тарас Шевченко", 1814)

# Книги
book1 = Book("Маруся Чурай", author1, 1979, "Історичний роман у віршах.")
book2 = Book("Кобзар", author2, 1840)
book3 = Book("Берестечко", author1, 1999)

# Бібліотека
library = Library("Національна бібліотека України")

# Додаємо книги
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Вивід усіх книг
print("📚 Усі книги в бібліотеці:")
for info in library.list_books():
    print(info)
    print()

# Пошук за автором
print("🔍 Книги Ліни Костенко:")
for info in library.find_books_by_author("Ліна Костенко"):
    print(info)
    print()

# Автори існують незалежно
print("👤 Інформація про авторів:")
print(author1.get_info())
print(author2.get_info())
