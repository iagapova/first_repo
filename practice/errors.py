def image_info(img):
    if 'image_title' not in img:
        raise TypeError(
            f"Key 'image_title' is absent in dictionary: \n{img}")
    elif 'image_id' not in img:
        raise TypeError(
            f"Key 'image_id' is absent in dictionary: \n{img}")
    return f"Image '{img['image_title']}' has id '{img['image_id']}'"


my_dict1 = {'image_id': 123,
            'image_title': 'My cat'}

my_dict2 = {'image_id': 12345}

my_dict3 = {'image_title': 'My dog.png'}

try:
    # print(image_info(my_dict1))
    # print()
    # print(image_info(my_dict2))
    # # print()
    print(image_info(my_dict3))
    # print()
    # image_info({'a': 1})
except TypeError as e:
    print(e)
# except KeyError
