def sq(n):
    result = n ** 2
    return result


nums = range(10)

for a in nums:
    print('a:', a)
    b = sq(a)
    print('a^2:', b)
