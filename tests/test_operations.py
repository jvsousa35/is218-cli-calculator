import pytest

from calculator.operations import Operations


def test_add():
    assert Operations.add(5, 3) == 8
    assert Operations.add(-5, 3) == -2
    assert Operations.add(2.5, 1.5) == 4
    assert Operations.add(0, 0) == 0


def test_subtract():
    assert Operations.subtract(10, 4) == 6
    assert Operations.subtract(-5, 3) == -8
    assert Operations.subtract(2.5, 1.5) == 1
    assert Operations.subtract(0, 0) == 0


def test_multiply():
    assert Operations.multiply(4, 3) == 12
    assert Operations.multiply(-4, 3) == -12
    assert Operations.multiply(2.5, 2) == 5
    assert Operations.multiply(5, 0) == 0


def test_divide():
    assert Operations.divide(10, 2) == 5
    assert Operations.divide(-10, 2) == -5
    assert Operations.divide(2.5, 2) == 1.25


def test_divide_by_zero():
    with pytest.raises(
        ValueError,
        match="Cannot divide by zero"
    ):
        Operations.divide(10, 0)
