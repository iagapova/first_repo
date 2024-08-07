class ExceptionPrint(Exception):
    "Бозовый класс ошибок принтера"
    pass


class ExceptionPrintSendData(ExceptionPrint):
    "Класс исключения при отправке данных принтеру"

    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f"Ошибка: {self.message}"


class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f"Печать: {str(data)}")

    def send_data(self, data):
        if not self.send_to_print(data):
            raise ExceptionPrintSendData("принтер не отвечает")

    def send_to_print(self, data):
        return False


p = PrintData()
try:
    p.print("123")
except ExceptionPrintSendData:
    print("принтер не отвечает")
except ExceptionPrint:
    print("ошибка")
