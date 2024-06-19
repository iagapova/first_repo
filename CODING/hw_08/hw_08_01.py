from datetime import datetime


def get_days_from_today(date):
    # сплитим дату в список
    t = date.split('-')
    # получаем формат даты в виде  2024-10-03 и откидываем времени
    input_date = datetime(year=int(t[0]), month=int(
        t[1]), day=int(t[2])).date()
    # получаем текущую дату + откидываем формат времени
    current_datetime = datetime.now().date()
    dif = current_datetime - input_date
    return dif.days
