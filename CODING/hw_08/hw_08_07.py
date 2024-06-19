import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats):

    if isinstance(cats[0], dict):
        # погнали со словарями
        print('погнали со словарями')
        result = []
        for item in cats:
            i = tuple(item.values())
            # print('---', i)
            # print()
            result.append(Cat(i[0], i[1], i[2]))
        return result
    elif isinstance(cats[0], Cat):
        # погнали со именованными кортежами
        print('погнали со именованными кортежами')
        result = []
        for item in cats:
            result.append({"nickname": item.nickname,
                          "age": item.age, "owner": item.owner})
        return result
    else:
        return []
