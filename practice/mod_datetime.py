from datetime import date, time, datetime, timedelta

print(date.today())   # Виводить поточну дату 2023-11-21
print('weekday = ', date.today().strftime('%A'))  # Tuesday
print('weekday = ', date.today().strftime('%a'))  # Tue
print('monthday = ', date.today().strftime('%B'))  # November
print('monthday = ', date.today().strftime('%b'))  # Nov
print('year = ', date.today().strftime('%y'))  # 23
print('fulldate = ', date.today().strftime(
    "%d/%m/%Y, %H:%M:%S"))  # 21/11/2023, 00:00:00

print('year = ', date.today().year)  # date.today().strftime('%Y')
print('month = ', date.today().month)
print('day = ', date.today().day)
print('year = ', date.today().strftime('%A'))

print()
current_time = time(12, 30, 45)
print(current_time)  # Виводить час 12:30:45
print()


print('now = ', datetime.now())  # Виводить поточну дату та час
print('now = ', datetime.now().strftime("%H:%M:%S"))  # 15:22:39
# 21 Nov, Tuesday 23, 15:22:39
print('now = ', datetime.now().strftime("%d %b, %A %y, %H:%M:%S"))
