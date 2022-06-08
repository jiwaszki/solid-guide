from operations import interface


class Summation(interface.Operation):
    def __init__(self, args):
        self.__args__ = args

    def calculate(self) -> int:
        return sum(map(lambda el: int(el), self.__args__))
