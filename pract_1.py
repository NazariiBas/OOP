class Book:
    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

    def get_info(self):
        return f"Назва: [{self.title}], Автор: [{self.author}], Рік видання: [{self.year}], Сторінок: [{self.pages}]"

    def is_modern(self):
        return self.year > 2010


#Приклад створення об'єктів та тестування методів
book1 = Book("Майстер і Маргарита", "Михайло Булгаков", 1967, 384)
book2 = Book("Підсвідомий розум", "Джозеф Мерфі", 2015, 320)

print(book1.get_info())
print("Сучасна книга?" , book1.is_modern())

print(book2.get_info())
print("Сучасна книга?" , book2.is_modern())