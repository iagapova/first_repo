def get_emails(list_contacts):
    result = []
    for item in map(lambda i: i.get("email", ), list_contacts):
        result.append(item)
    return result
