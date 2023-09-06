import re


def find_all_links(text):
    result = []
    iterator = re.finditer(r"((?:https|http):\/\/(?:[a-zA-Z0-9]+\.{1}[a-zA-Z0-9]+\.{1}[a-zA-Z0-9]+|[a-zA-Z0-9]+\.{1}[a-zA-Z0-9]+))", text)
    for match in iterator:
        result.append(match.group())
    return result









