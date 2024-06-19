def caching_fibonacci():
    cache = {}

    def fibonachi(n):
        # проверка есть ли в кеше
        if n in cache.keys():
            return cache[n]
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            # добавляем в кеш
            cache[n] = fibonachi(n-1) + fibonachi(n-2)
            print(cache)
            return cache[n]
    return fibonachi


# начальный кеш
fibonacci = caching_fibonacci()
print(fibonacci(5))
