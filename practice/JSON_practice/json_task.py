import json
from textwrap import indent

my_dict = {'Car': 'Ford',
           'brand': 'Edge',
           'ready_to_go': False,
           'year': 2018,
           'voltage': None,
           'days_to_fix': [1, 2, 2.5],
           'type': {'first': 'No', 'second': 'No', 'third': 'Yes'}
           }

print(my_dict)
print()
my_json = json.dumps(my_dict, indent=1)
print(my_json)
print(type(my_json))
