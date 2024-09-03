from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass


class ConsoleLogger(Logger):
    def log(self, message):
        print(message)


class FileLogger(Logger):
    def __init__(self, filename):
        self.filename = filename

    def log_to_file(self, message):
        with open(self.filename, 'w') as file:
            file.write(message)
