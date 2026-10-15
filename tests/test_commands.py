import pytest

from calculator.operations import Operations
from calculator.calculation import ArithmeticCalculation
from calculator.commands import CalculateCommand, HistoryCommand


def test_calculate_command():
    history = []
    calculation = ArithmeticCalculation.create(
        5, 3, Operations.add
    )

    command = CalculateCommand(calculation, history)

    assert command.execute() == 8
    assert history == ["5 add 3 = 8"]


def test_multiple_history_entries():
    history = []

    first = ArithmeticCalculation.create(
        5, 3, Operations.add
    )
    second = ArithmeticCalculation.create(
        10, 4, Operations.subtract
    )

    CalculateCommand(first, history).execute()
    CalculateCommand(second, history).execute()

    assert len(history) == 2
    assert history[0] == "5 add 3 = 8"
    assert history[1] == "10 subtract 4 = 6"


def test_failed_calculation_not_saved():
    history = []
    calculation = ArithmeticCalculation.create(
        10, 0, Operations.divide
    )

    command = CalculateCommand(calculation, history)

    with pytest.raises(ValueError):
        command.execute()

    assert history == []


def test_empty_history():
    history = []

    command = HistoryCommand(history)

    assert command.execute() == []


def test_history_returns_copy():
    history = ["5 add 3 = 8"]

    command = HistoryCommand(history)
    result = command.execute()

    result.append("Extra entry")

    assert history == ["5 add 3 = 8"]
    assert len(result) == 2
