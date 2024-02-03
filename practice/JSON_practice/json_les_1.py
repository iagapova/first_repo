import json

json_str = '{"abc":25, "status":false, "info":{"type":"pass"}}'

my_dict = json.loads(json_str)

print(my_dict)

new_json1 = json.dumps(my_dict)

print(new_json1)

new_json2 = json.dumps(my_dict, indent=1)
print(new_json2)
