def route_info(my_dict):
    if ('distance' in my_dict and type(my_dict['distance']) == int):
        return f"Distance to your destination is {my_dict['distance']}"
    if ('speed' in my_dict and 'time' in my_dict and type(my_dict['speed']) == int and type(my_dict['time']) == int):
        return f"Distance to your destination is {my_dict['speed']*my_dict['time']}"
    return "No distance info is available"


d1 = {
    'car': 'Ford',
}

d2 = {
    'car': 'Ford',
    'distance': True
}

d3 = {
    'car': 'Ford',
    'distance': 25
}

d4 = {
    'speed': 3,
    'time': 25
}
print(route_info(d4))

text = "эолвролва лорвало варл"
print('String is long') if len(text) > 25 else print('String is short')

print('String is long' if len(text) > 25 else 'String is short')

info = 'String is long' if len(text) > 25 else 'String is short'
print(info)
