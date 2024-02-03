class Car:
    def move(self):
        print("Car is moving")

    def stop(self):
        print("Car stopped")


my_car = Car()
print(type(my_car))
print(isinstance(my_car, Car))
my_car.move()
my_car.stop()

# Определяем класс и создаем экземпляр через функцию __init__


class Comment:
    def __init__(self, text):
        self.text = text  # собственные обьекты класса
        self.votes_qty = 0  # собственные обьекты класса

    def upvote(self, num):
        self.votes_qty += num

    # добавление магического оператора сравнения
    def __eq__(self, other):
        pass
        return True if self.votes_qty == other.votes_qty else False

    # добавление магического оператора добавления
    def __add__(self, other):
        pass
        return [self.text + ' ' + other.text, self.votes_qty + other.votes_qty]
        # return f"{self.text} {other.text}, {self.votes_qty + other.votes_qty}"

    # определение статического метода
    @staticmethod
    def merge_comments(first, second):
        return f"{first}{second}"


first_comment = Comment('First comment')  # тут вызыввается метод __init__
print(first_comment.text)
print(first_comment.votes_qty)
# проверка собственных аттрибутов
print(first_comment.__dict__)
print()

first_comment.upvote(5)
print(first_comment.votes_qty)

first_comment.qty = 10  # добавили еще один аттрибут
print(first_comment.__dict__)

# использование статических методов
m_1 = Comment.merge_comments("Hi,", "Iryna!")
print(m_1)
m_2 = first_comment.merge_comments("Hi,", "Iryna!")
print(m_2)

print(first_comment.__dict__)

second_comment = Comment('Second comment')
print(second_comment)
print(second_comment.votes_qty)
second_comment.upvote(5)
print(second_comment.votes_qty)

# после магической операции сравнения __or__
print(first_comment == second_comment)

# после магической операции добавления __add__
print(first_comment + second_comment)
