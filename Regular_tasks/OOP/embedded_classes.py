class Women:
    title = 'обьект класса для поля title'
    photo = 'обьект класса для поля photo'
    ordering = 'обьект класса для поля ordering'

    def __init__(self, user, psw):
        self._user = user
        self._psw = psw
        # !только благодаря этой строчке создастся обьект класса Meta
        self.meta = self.Meta(user + '@' + psw)

    class Meta:
        ordering = ['id']

        def __init__(self, access):
            self._access = access
            # получить доступ к аттрибуту внешнего класса можно только в __init__
            self._t = Women.title
            # Но это плохая практика обращаться к аттрибутам внешнего класса из внутреннего


m = Women('root', '1234')
print(m.ordering)
print(m.Meta.ordering)
print(m.__dict__)
print(m.meta.__dict__)
