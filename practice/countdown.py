from time import time, sleep
from datetime import datetime


final_time = datetime(2024, 7, 8, 15, 28, 00)  # вводим нужное время
print("Alarm at: ", final_time)
final_time_timestamp = final_time.timestamp()  # получаем таймстемп от времени
# print(final_time_timestamp)

current_time = time()
# print(current_time)


if round(final_time_timestamp - current_time) > 0:
    print(
        f"Наш отсчет пошел, осталось всего: {round(final_time_timestamp - current_time)} секунд")
    while final_time_timestamp >= current_time:
        i = final_time_timestamp - current_time
        print(round(i))  # наш вывод счетчика
        sleep(1)
        current_time = time()  # получаем свежже текущее время
    print('ШАРАХ!')
else:
    print('Сорян, указанное время уже в прошлом')
