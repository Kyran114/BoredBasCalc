import Calculator

run = int(1)
while run > 0:
    try:
        cal =Calculator.Calculator()
        print("-------------------------------")
        print("Welcome to the Calculator :)")
        print("-------------------------------")
        var1 = int(input("Variable 1: "))
        var2 = int(input("Variable 2: "))
        print("-------------------------------")
        print("Please enter: the desired operator choice as a number: ")
        print("1:Add  2:Sub  3:Mult  4:Div")
        print("-------------------------------")
        operator = int(input())
        print("-------------------------------")
        print("Calculating...")
        if operator == 1 :
            print(f"The result = {cal.add(var1, var2)}")
            pass
        elif operator == 2:
            print(f"The result = {cal.sub(var1, var2)}")
            pass
        elif operator == 3:
            print(f"The result = {cal.mult(var1, var2)}")
            pass
        elif operator == 4:
            print(f"The result = {cal.div(var1, var2)}")
            pass
        else:
            print("Invalid Number, try again")
            continue
            
    except Exception as e:
            print("Error: ", e)
            continue
    try:
        print("-------------------------------")
        print("Another Calculation ?")
        print("Please enter your choice as a number: ")
        print("-------------------------------")
        print("1.Yes")
        print("2.No") 
        print("-------------------------------")
        dec = int(input("Your choice = "))
        if dec == 1:
            continue
        elif dec == 2:
            print("Good Bye")
            exit()
        else:
            print("Invalid Operator, try again")
            continue

    except Exception as e:
        print("Invalid Operator")
        break


                
        

        

    


    
    
    
