from abc import ABC, abstractmethod
from collections.abc import Callable


class Calculation(ABC):
    def __init__(
        self,
        a: float,
        b: float,
        operation: Callable[[float, float], float]
    ):
        # Each instance stores its own values.
        self.a = a
        self.b = b
        self.operation = operation

    @classmethod
    def create(cls, a, b, operation):
        # cls creates an instance of the calling class.
        return cls(a, b, operation)

    @abstractmethod
    def execute(self) -> float:  # pragma: no cover
        # Abstract placeholder; subclasses implement this.
        pass

class ArithmeticCalculation(Calculation):
    def execute(self) -> float:
        # Uses this instance's stored values.
        return self.operation(self.a, self.b)
