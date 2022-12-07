
import sys

def basic_calc(op, val1, val2):
    # Check inputs are ints

    # Perform operation
    if(op == '/'):
        retval = val1 / val2
    elif(op == 'x'):
        retval = val1 * val2
    elif(op == '+'):
        retval = val1 + val2
    elif(op == '-'):
        retval = val1 + val2
    elif(op == '%'):
        retval = val1 % val2
    else:
        retval = ("Error: no valid operator supplied")
    return retval

def main(argv):
    # Test cases
    print(basic_calc('+',1,2))
    print(basic_calc('/',5,2))
    print(basic_calc('x',5,0))
    print(basic_calc('%',10,3))

    with open("step_2.txt", 'r') as f:
        lines = f.readlines()

    line = 1
    #while (line < len(lines))


if __name__ == "__main__":
   main(sys.argv)