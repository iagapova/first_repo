aaa = [0, 1, 3, 2, 0, 2]
points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    if coordinates == []:
        return 0
    else: 
        s = 0
        for i in range(0, len(coordinates) - 1):
            coord = ((min(coordinates[i], coordinates[i+1]), max(coordinates[i], coordinates[i+1])))
            for key, value in points.items():
                if coord == key:
                    s += value
        # print(s)
        return s
        
calculate_distance(aaa)