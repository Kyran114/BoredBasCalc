import Calculator
import time
from art import *

def run():
    run = True
    while run == True:
        try:
            cal =Calculator.Calculator()
            print("-------------------------------")
            tprint("Calculator", font="doom  ")
            print("-------------------------------")
            var1 = int(input("Variable 1: "))
            var2 = int(input("Variable 2: "))
            print("-------------------------------")
            print("Please enter: the desired operator choice as a number: ")
            print("1:Add  2:Sub  3:Mult  4:Div")
            print("-------------------------------")
            operator = int(input("Your choice = "))
            print("-------------------------------")

            Operations = {1: "Addition", 2: "Subtraction", 3: "Multiplication", 4: "Division"}
            if operator in Operations :
                tprint("Calculating...", font="doom  ")
                time.sleep(1)
                match (operator):
                    case (1):
                        print(f"The result = {cal.add(var1, var2)}")
                        pass
                    case (2):
                        print(f"The result = {cal.sub(var1, var2)}")
                        pass
                    case (3):
                        print(f"The result = {cal.mult(var1, var2)}")
                        pass
                    case (4):
                        print(f"The result = {cal.div(var1, var2)}")
                        pass
            else:
                print("Invalid Selection, try again")
                continue
        except Exception as e:
            print("Error: ", e)
            continue
        try:
            time.sleep(1)
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
                run = False
                exit()
            else:
                print("Invalid Operator, try again")
                continue

        except Exception as e:
            print("Invalid Operator")
            break

if __name__ == "__main__":
    # Code
    run()


                
        

        

    


    
    
    
