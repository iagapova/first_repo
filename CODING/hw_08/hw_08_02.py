from datetime import date


def get_days_in_month(month, year):

    # получаем формат даты в виде  2024-01-01
    input_date = date(year, month, 1)
    # если декабрь - увеличиваем год, скидываем на январь
    if month == 12:
        next_month = date(year + 1, 1, 1)
    else:
        # если не декабрь - увеличиваем месяц
        next_month = date(year, month + 1, 1)
    return (next_month - input_date).days
