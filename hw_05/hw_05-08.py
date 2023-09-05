grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    s = []
    i = 1  # Переменная для нумерации строк  
    # Перебираем элементы словаря students
    for student, grade in students.items():
        # Получаем оценку из словаря grades
        grade_value = grades.get(grade, None) 
        #n = ("{:>4}|{:<10}|{: ^5}|{: ^5}".format(i, student, grade, grade_value))
        #formatted_row = f"{row_number}|{student:<10}| {grade}  | {grade_value}"
        
        # Форматируем строку и добавляем её в список
        n = f"{i:>4}|{student:<10}|{grade:^5}|{grade_value: ^5}"
        s.append(n)
        i += 1 
    return s
        
    
students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
for el in formatted_grades(students):
   print(el)