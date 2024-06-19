import base64


def encode_data_to_base64(data):
    new_list = []
    for item in data:
        item_bytes = item.encode()
        base64_bytes = base64.b64encode(item_bytes)
        base64_item = base64_bytes.decode()
        new_list.append(base64_item)
    return new_list


data = ['andry:uyro18890D', 'steve:oppjM13LL9e']
print(encode_data_to_base64(data))
