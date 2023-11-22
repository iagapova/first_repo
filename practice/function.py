def increase_age(person):
    person_new = person.copy()
    person_new['age'] += 1
    return person_new


person_one = {
    'name': 'Iryna',
    'age': 20
}

person_two = increase_age(person_one)
print(person_one)
print(person_two)
