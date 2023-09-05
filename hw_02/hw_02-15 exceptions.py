result = None
operand = None 
operator = None
wait_for_number = True
s = ''
while True:
    num = input('Enter value: ')
    if num == '=':
        break
    elif wait_for_number == True: # ищем цифру
        if num.isdigit(): # и это цифра
            try:
                operand = num # присваиваем значение 
                s1 = s + str(operand)
                result = eval(s1)
                print('current result= ', result)
                s = str(result)
                wait_for_number = False
            except ZeroDivisionError:
                print("Ай-ай, делить на 0 не хорошо!")
        else: # ищем цифру, но это не цифра
            print(num, " is not a number. Try again.")
    else: # не ищем цифру
        if num in ['+', '-', '/', '*']: # и это оператор
            operator = num
            s1 = s + str(operator)
            s = s1
            wait_for_number = True
        else: # ищем цифру, но это не цифра
            print(num, " is not '+' or '-' or '/' or '*'. Try again")
print('Result = ', result)
    
        
    
        
            
        
            
            
        
        
            
        
            
                
            
                
            
                
            
                
    
        
                
                
                
                
        
            
        
            

        
            
        
            