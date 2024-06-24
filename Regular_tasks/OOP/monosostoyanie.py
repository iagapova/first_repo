class TrheadData:
    # локальное свойство имен едино для экземпляров класса
    __shared_attr = {
        'name': 'thread_1',
        'data': {},
        'id': 1
    }

    def __init__(self):
        self.__dict__ = self.__shared_attr


tr_1 = TrheadData()
tr_2 = TrheadData()
print(f"tr_1.id = {tr_1.id}, tr_2.id = {tr_2.id}")
tr_1.id = 5
print(f"tr_1.id = {tr_1.id}, tr_2.id = {tr_2.id}")
print(tr_2.id)
tr_2.new_attr = 'abc'
print(f"tr_1.new_attr = {tr_1.new_attr}, tr_2.new_attr = {tr_2.new_attr}")
