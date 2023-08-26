all_energy = [[1, 1, 5, 10], [10, 2], [1, 1, 1]]
power = 1
def game(terra, power):
    for i in range(len(terra)):
        for j in terra[i]:
            if j <= power:
                power += j
                print('слопали ', j , ' = ' , power)
            else: 
                print('уходим из ', terra[i], 'потому что ', power, ' меньше ', j )
                break
    print('ИТОГО: ', power)
    return power  
  
game(all_energy, power)