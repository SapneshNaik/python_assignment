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

    choice = None

    while choice is not 5:
        
        try:
            choice = int(input("\nEnter choice\n"))

            #check if valid choice
            if not valid_choice(choice):
                print("Invalid choice")
                continue

            if choice == 5:
                print("\nBye\n")
                break

            num1 = int(input("Enter first number\n"))   
            num2 = int(input("Enter second number\n"))
        except:
            print("Invalid number.. ")
            continue


        if choice is 1:
            print( "\n Answer : ",Calculator.add(num1, num2))

        if choice is 2:
                print( "\n Answer : ",Calculator.subtract(num1, num2))

        if choice is 3:
                print( "\n Answer : ",Calculator.multiply(num1, num2))

        if choice is 4:
            if num2 == 0:
                print("\n Cannot divide by zero!")
                continue

            print( "Answer : ",Calculator.division(num1, num2))


if __name__ == "__main__":
    main()