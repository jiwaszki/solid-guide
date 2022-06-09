import sys
import argparse
from docs.MyFunctions import funcs


def main() -> int:
    """Main function..."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-fn", "--functionName", dest="fn", type=str,
                        help="Name of funciton to use.\n"+
                        "Avaible function names are:\n"+
                        "Add\n"+
                        "Subtract\n"+
                        "Multiply\n"+
                        "Divide\n")
    parser.add_argument("-a", "--aValue", dest="a", type=float, help="a value of float type")
    parser.add_argument("-b", "--bValue", dest="b", type=float, help="b value of float type")
    args = parser.parse_args()

    
    print("Provided function name:",end="")
    print(args.fn)
    print("First provided value of type float:",end="")
    print(args.a)
    print("Second provided value of type float:",end="")
    print(args.b)

    myFuncFactory=[]
    myFuncFactory.append([funcs.MyAdd.calculate(args.a,args.b),"Add"])
    myFuncFactory.append([funcs.MySubtract.calculate(args.a,args.b),"Subtract"])
    myFuncFactory.append([funcs.MyMultiply.calculate(args.a,args.b),"Multiply"])
    myFuncFactory.append([funcs.MyDivide.calculate(args.a,args.b),"Divide"])
    for i in range(0, len(myFuncFactory)):
        if(myFuncFactory[i][1]==args.fn):
            print("Result:")
            return myFuncFactory[i][0]

    return "Provided Function Name Does not exist or parsed values were wrong."


if __name__ == "__main__":
    sys.exit(main())
