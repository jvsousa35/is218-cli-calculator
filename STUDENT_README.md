# CLI Calculator — IS218

## Project Overview

This project is a command-line calculator built using Python. It 
supports addition, subtraction, multiplication, and division, while 
demonstrating object-oriented programming, design patterns, 
automated testing, and calculation history.

## Setup

Python 3.12 or newer is required.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Running the Calculator

```bash
python -m calculator
```

Example commands:

```text
add 5 3
subtract 10 4
multiply 2 6
divide 10 2
history
exit
```

The calculator supports decimals, negative numbers, and error 
handling for invalid commands, invalid operands, and division by 
zero.

## Testing

Run:

```bash
python -m pytest --cov=calculator --cov-report=term-missing 
--cov-fail-under=100
```

The project includes 23 automated tests and has achieved 100% line 
coverage locally.

## Object-Oriented Programming Concepts

**Encapsulation:** The Calculation class stores the operands and 
operation together. HistoryCommand protects the original history 
list by returning a copy.

**Abstraction:** Calculation is an abstract base class that 
requires subclasses to implement execute().

**Inheritance:** ArithmeticCalculation inherits from Calculation 
and reuses its factory method.

**Polymorphism:** Different calculation implementations can provide 
their own execute() behavior while following the same interface.

**Composition:** CalculateCommand contains a calculation object, 
while ArithmeticCalculation contains an operation function.

## SOLID Principles

**Single Responsibility:** Operations performs arithmetic, 
Calculation represents a calculation, CalculateCommand manages 
execution and history, and the CLI handles user interaction.

**Open/Closed:** Additional operations can be introduced without 
rewriting the calculation execution logic.

**Liskov Substitution:** A concrete Calculation implementation must 
follow the execute() contract and return a numeric result or raise 
an appropriate error.

**Interface Segregation:** The Calculation interface requires only 
execute(), avoiding unnecessary methods.

**Dependency Inversion:** CalculateCommand receives a Calculation 
abstraction rather than creating a specific arithmetic calculation 
internally.

## Method Types

**Static Methods:** Operations uses static methods because 
arithmetic functions do not require object state.

**Class Methods:** Calculation.create() uses cls to create an 
instance of the calling class.

**Instance Methods:** ArithmeticCalculation.execute() uses the 
instance's stored operands and operation.

## Design Patterns

**Factory Pattern:** ArithmeticCalculation.create() constructs 
calculation objects.

**Command Pattern:** CalculateCommand executes calculations and 
records successful results. HistoryCommand retrieves calculation 
history.

**Strategy Pattern:** The CLI selects an operation function from a 
dictionary based on the user's command. The calculation executes 
the selected operation without needing separate calculation logic 
for each operation.

Addition, subtraction, multiplication, and division all use the 
same calculation execution method. Only the selected operation 
function changes.

## Coverage Exclusions

The abstract execute() placeholder is excluded from coverage 
because it has no executable implementation.

The package entry-point code in __main__.py is excluded because the 
CLI behavior is tested directly through main().

## GitHub Actions

GitHub Actions automatically runs the tests on Python 3.12 and 
requires 100% line coverage.

**Successful workflow run:** Add the link to the successful GitHub 
Actions run after pushing the completed project.
