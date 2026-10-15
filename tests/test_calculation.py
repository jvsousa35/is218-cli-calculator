import pytest

from calculator.calculation import (
    Calculation,
    ArithmeticCalculation,
)
from calculator.operations import Operations


def test_factory():
    calculation = ArithmeticCalculation.create(
        5, 3, Operations.add
    )

    assert isinstance(calculation, ArithmeticCalculation)
    assert calculation.a == 5
    assert calculation.b == 3
    assert calculation.operation == Operations.add


def test_abstract_class():
    with pytest.raises(TypeError):
        Calculation(5, 3, Operations.add)


def test_add_calculation():
    calculation = ArithmeticCalculation.create(
        5, 3, Operations.add
    )
    assert calculation.execute() == 8


def test_subtract_calculation():
    calculation = ArithmeticCalculation.create(
        10, 4, Operations.subtract
    )
    assert calculation.execute() == 6


def test_multiply_calculation():
    calculation = ArithmeticCalculation.create(
        4, 3, Operations.multiply
    )
    assert calculation.execute() == 12


def test_divide_calculation():
    calculation = ArithmeticCalculation.create(
        10, 2, Operations.divide
    )
    assert calculation.execute() == 5


def test_calculation_error():
    calculation = ArithmeticCalculation.create(
        10, 0, Operations.divide
    )

    with pytest.raises(ValueError):
        calculation.execute()
