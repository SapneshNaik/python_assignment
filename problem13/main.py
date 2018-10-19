#Python does not have switch or case statement. 
#However the functionality can be mimicked using a dictionary

import sys
from calculator import Calculator

def show_choices():
    print(" 1 - Addition")      
    print(" 2 - Subtraction")       
    print(" 3 - Multiply")
    print(" 4 - Division")      
    print(" 5 - Quit")

def valid_choice(choice):
    return True if (choice >= 1) and (choice <= 5) else False

def main():

    show_choices()
    
    try:
        choice = int(input("\nEnter choice\n"))
    except:
        print("Invalid number.. ")
        sys.exit()

    #check if valid choice
    if not valid_choice(choice):
        print("Invalid choice")
        sys.exit()

    if choice == 5:
        print("\nBye\n")
        sys.exit()

    try:
        num1 = int(input("Enter first number\n"))   
        num2 = int(input("Enter second number\n"))
    except:
        print("Invalid number.. ")
        sys.exit()


    #Note all the method calls are executed during run time regardless of the choice value
    switch = {
    	1: Calculator.add(num1, num2),
    	2: Calculator.subtract(num1, num2),
    	3: Calculator.multiply(num1, num2),
    	4: Calculator.division(num1, num2),
    }

    print( "Answer is", switch.get(choice) )


if __name__ == "__main__":
    main()
