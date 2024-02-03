class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        DataBase.__instance = None


db = DataBase(1, 2)
db2 = DataBase(3, 4)

print(id(db), id(db2))
