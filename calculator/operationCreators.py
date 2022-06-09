import calculator.operations as  ops
from abc import ABC, abstractmethod

class CreateOperation(ABC):
    @abstractmethod
    def factory_method(self, args):
        pass
    def calculate(self, args):
        operation = self.factory_method(args)
        return operation.calculate()

class CreateSummation(CreateOperation):
    def factory_method(self, args) -> ops.Operation:
        return ops.Summation(args)

class CreateSubtraction(CreateOperation):
    def factory_method(self, args) -> ops.Operation:
        return ops.Subtraction(args)