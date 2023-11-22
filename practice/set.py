a = {1, 2, 3, 4}

a.add(5)

print('список a = ', a)

b = {2, 0, -2, 4, 10}
print('список b = ', b)

с = a.union(b)
print('список объединяющий a и b: c = ', с)

d = a.intersection(b)
print('список пересечений a и b: d = ', d)
