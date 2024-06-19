def get_favorites(contacts):
    result = []
    for item in filter(lambda i: i["favorite"] == True, contacts):
        result.append(item)
    return result
