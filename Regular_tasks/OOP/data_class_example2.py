from dataclasses import dataclass, field, InitVar


@dataclass
class Book:
    title: str
    author: str
    isbn: str
    pages: int
    available: bool = field(default=True)

    def __post_init__(self):
        if self.pages <= 0:
            raise ValueError("Количество страниц должно быть положительным")


@dataclass
class LibraryUser:
    user_id: str
    name: str
    email: str
    borrowed_books: list = field(default_factory=list)

    def borrow_book(self, book: Book):
        if book.available:
            self.borrowed_books.append(book)
            book.available = False
            print(f'Отдаем книгу "{book.title}" юзеру {user1.name}')
        else:
            print(f"Книга '{book.title}' недоступна")

    def return_book(self, book: Book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True
            print(f'Юзер {user1.name} возвращает книгу "{book.title}" ')
        else:
            print(f"Книга '{book.title}' не найдена в списке взятых книг")


book1 = Book("Война и мир", "Лев Толстой", "978-5-17-118366-4", 1225)
book2 = Book("1984", "Джордж Оруэлл", "978-0-452-28423-4", 328)
book3 = Book("Мастер и Маргарита", "Михаил Булгаков",
             "978-5-389-07416-3", 480)
print(book1)
print(book2)
print(book3)
print()
user1 = LibraryUser("U001", "Иван Иванов", "ivan@example.com")
print(user1)
print()
user1.borrow_book(book2)
print()
print(f'Теперь статус книги у нас: {book2.available}')
print(f'Книги у юзера1:')
print(user1.borrowed_books)
print('-----------------')
print('Все книги:')
print(book1)
print(book2)
print(book3)
print('-----------------')
print()
user1.return_book(book2)
print()
print('Теперь статус книги у нас:')
print(book2.available)
print(f'Книги у юзера1:')
print(user1.borrowed_books)
print()
print('-----------------')
print('Все книги:')
print(book1)
print(book2)
print(book3)
print('-----------------')
