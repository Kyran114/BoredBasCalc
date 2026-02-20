class Calculator():
    result = 0
    def add(self):
        result =var1 + var2
        return result
    
    def sub(self):
        result =var1 - var2
        return result
    
    def mult(self):
        result =var1 * var2
        return result
    
    def div(self):
        result =var1 / var2
        return result

run = int(1)
while run != 0:
        var1 = int(input("Please enter: Variable 1 = "))
        var2 = int(input("Please enter: Variable 2 = "))
        print("1.Add")
        print("2.Sub")
        print("3.Mult")
        print("4.Div")
        operator = input("Please enter: the desired operator choice = ")
        cal =Calculator()
        if operator == 1 :
            print(cal.add())
        elif operator == 2:
            print(cal.sub())
        elif operator == 3:
            print(cal.mult())
        elif operator == 4:
            print(cal.div())
        else:
            print("invalid operator")
        dec = input("Another Calculation ?")
        print("1.Yes")
        print("2.No") 
        if dec == "Y"or "y":
            run = 1
        elif dec == "N" or "n":
            run = 0
            exit

        

    


    
    
    
