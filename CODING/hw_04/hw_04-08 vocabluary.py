def game(terra, power):
    for i in range(len(terra)):
        for j in terra[i]:
            if j <= power:
                power += j
                # print('слопали ', j , ' = ' , power)
            else: 
                # print('уходим из ', terra[i], 'потому что ', power, ' меньше ', j )
                break
    # print('ИТОГО: ', power)
    return power  