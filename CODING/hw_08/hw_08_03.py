from datetime import datetime


def get_str_date(date):
    # преобразовываем из ISO в тип datetime (убирая последний символ)
    my_date = datetime.fromisoformat(date[:-1])
    # преобразуем в формат Tuesday 07 January 2020
    return my_date.strftime('%A %d %B %Y')
