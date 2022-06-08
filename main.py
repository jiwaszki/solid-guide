import sys
import argparse
from operations import addition


def main(args) -> int:
    """Main function..."""

    print(args)

    # instancja dodawania
    suma1 = addition.Summation(args.val)
    print(suma1.calculate())

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--suma", nargs="*", dest="val")
    args = parser.parse_args()
    sys.exit(main(args))
