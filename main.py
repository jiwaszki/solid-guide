import argparse, sys
from calculator.operationCreators import CreateSummation, CreateSubtraction


def main(args) -> int:
    print(args.op.calculate(args.nums))

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-a", "--add", dest="op", action="store_const", const=CreateSummation(), help="add arguments")
    group.add_argument("-s", "--sub", dest="op", action="store_const", const=CreateSubtraction(), help="subtract arguments")
    group.set_defaults(op=CreateSummation())
    parser.add_argument("nums", metavar="N", nargs="+", type=float, help="n arguments")
    args = parser.parse_args()

    sys.exit(main(args))
