def get_grade(key):
    grade = {"F":1, "FX":2, "E":3, "D":3, "C":4, "B":5, "A":5}
    s = grade.get(key, None)
    return s


def get_description(key):
    grade = {"F":"Unsatisfactorily", "FX":"Unsatisfactorily", "E":"Enough", "D":"Satisfactorily", "C":"Good", "B":"Very good", "A":"Perfectly"}
    s = grade.get(key, None)
    return s