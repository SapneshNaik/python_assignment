import sys
import getopt
from calculator import Calculator

def usage():
    print("\nUsage: python ", sys.argv[0]," --num1 <integer> --num2 <integer> --op <operand>\n")
    print("Add: python ", sys.argv[0]," --python ", sys.argv[0]," --num1 10 --num2 10 --op +\n")
    print("Subtract: python ", sys.argv[0]," --num1 10 --num2 10 --op -\n")
    print("Multiply: python ", sys.argv[0]," --num1 10 --num2 10 --op \*\n")
    print("Divide: python ", sys.argv[0]," --num1 10 --num2 10 --op /\n")


def main(argv):

    try:
        (opts, args) = getopt.getopt(sys.argv[1:], 'ha:b:o', ['help','num1=', 'num2=', 'op='])
    #raised whenever an option (which requires a value) is passed without a value.
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)


    num1 = num2 = op = None
    if(len(opts) >= 3):
        try:
            for (o, a) in opts:
                if o in ('-h', '--help'):
                    usage()
                    sys.exit()
                elif o in ('-a', '--num1'):
                    num1 = float(a)
                elif o in ('-b', '--num2'):
                    num2 = float(a)
                elif o in '--op':
                    op = a
                else:
                    usage()
                    sys.exit(2) 

            #check if num1 and num2 and op not None
            if num1 and num2 and op:
                if(op == '+'):
                    print( "\n Answer : ",Calculator.add(num1 , num2))
                    return

                elif(op == '-'):
                    print( "\n Answer : ",Calculator.subtract(num1 , num2))
                    return

                elif(op == '*'):
                    print( "\n Answer : ",Calculator.multiply(num1 , num2))
                    return

                elif(op == '/'):
                    print( "\n Answer : ",Calculator.division(num1 , num2))
                    return

                else: usage()          
        except Exception as e:
            print(e)

    else:
        usage()

if __name__=="__main__":
    #exclude file name from args
    main(sys.argv)
