import sys
import argparse
from calculator import Calculator

def usage():
    print("\nUsage: python ", sys.argv[0]," --num1 <integer> --num2 <integer> --op <operand>\n")
    print("Add: python ", sys.argv[0]," --python ", sys.argv[0]," --num1 10 --num2 10 --op +\n")
    print("Subtract: python ", sys.argv[0]," --num1 10 --num2 10 --op -\n")
    print("Multiply: python ", sys.argv[0]," --num1 10 --num2 10 --op \*\n")
    print("Divide: python ", sys.argv[0]," --num1 10 --num2 10 --op /\n")


def main(argv):

    parser = argparse.ArgumentParser(description='CLA based calculator.')
    parser.add_argument('-n1', '--num1', metavar='num1', type=float, help='First number input', required=True)
    parser.add_argument('-n2', '--num2', metavar='num2', type=float, help='Second number input', required=True)
    parser.add_argument('--op', metavar='operand', help='operation ( +, -, \*, /)', required=True)

    try:
        args = parser.parse_args()
    except:
        usage()
        sys.exit()

    if(args.op == '+'):
        print( "\n Answer : ",Calculator.add(args.num1 , args.num2))
        return

    elif(args.op == '-'):
        print( "\n Answer : ",Calculator.subtract(args.num1 , args.num2))
        return

    elif(args.op == '*'):
        print( "\n Answer : ",Calculator.multiply(args.num1 , args.num2))
        return

    elif(args.op == '/'):
        print( "\n Answer : ",Calculator.division(args.num1 , args.num2))
        return

    else: usage()          

if __name__=="__main__":
    #exclude file name from args
    main(sys.argv)
