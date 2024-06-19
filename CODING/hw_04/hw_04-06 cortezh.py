grade = [2, 4, 6, 8, 10]

def split_list(grade):
    first = []
    second = []
    if grade == []:
        return first, second
    else:
        s = 0
        for i in grade:
            s += i
        average = s/len(grade)
        first = []
        second = []
        for i in grade:
            if i <= average:
               first.append(i)
            else: 
               second.append(i)
        return first, second
        
            
        
            
    