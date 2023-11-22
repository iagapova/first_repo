tup_one = ('one', 'Name', 25, True, 25, 0, False,
           25, -25, True, 25, 62, 'ddd', 25, 0, 25)
tup_two = ("some long text", {'Name': 'Iryna'})


print('вот что вышло: ')
print(tup_one + tup_two)

print(tup_one.count(25))
# print(tup_one.index(25), tup_one.index(25, tup_one.index(25) + 1),
#       tup_one.index(25, (tup_one.index(25, tup_one.index(25) + 1))+1))

i = 0
while i < len(tup_one) - 1:
    i = tup_one.index(25, i)
    print(i)
    i += 1
