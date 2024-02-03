# создаем подкласс класса list
class My_list(list):
    def count_cars(self):
        print(len(self))


my_autopark = My_list(['Aveo', 'Kuga', 'Edge'])
my_autopark.count_cars()
my_autopark.append('C-Max')
my_autopark.count_cars()
