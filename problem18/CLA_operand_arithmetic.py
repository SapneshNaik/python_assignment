import sys

from calculator import Calculator
def usage():
    print("\nUsage: file.py <operand> <operator> <operand>\n")
    print("Add: $ python file.py 5 + 10\n")
    print("Subtract: $ python file.py 5 - 10\n")
    print("Multiply: $ python file.py 5 \* 10\n")
    print("Divide: $ python file.py 5 / 10\n")


def main(argv):

    if(len(argv) >= 3):
        try:            
            if(argv[1] == '+'):
                print( "\n Answer : ",Calculator.add(float(argv[0]), float(argv[2])))
                return

            if(argv[1] == '-'):
                print( "\n Answer : ",Calculator.subtract(float(argv[0]), float(argv[2])))
                return

            if(argv[1] == '*'):
                print( "\n Answer : ",Calculator.multiply(float(argv[0]), float(argv[2])))
                return

            if(argv[1] == '/'):
                print( "\n Answer : ",Calculator.division(float(argv[0]), float(argv[2])))
                return

            usage()
        except:
            usage()

    else:
        usage()

if __name__=="__main__":
    #exclude file name from args
    main(sys.argv[1:])
