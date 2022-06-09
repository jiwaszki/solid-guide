from abc import ABC, abstractmethod
from functools import reduce
from dataclasses import dataclass

class Operation(ABC):
    @abstractmethod
    def calculate(self):
        pass

@dataclass(frozen=True)
class Summation(Operation):
    __args__: list
    def calculate(self):
        return sum(self.__args__)

@dataclass(frozen=True)
class Subtraction(Operation):
    __args__: list
    def calculate(self):
        return reduce(lambda acc, elem: acc - elem, self.__args__)