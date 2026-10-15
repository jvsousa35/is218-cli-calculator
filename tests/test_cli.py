import builtins

from calculator.cli import main


def run_cli(monkeypatch, commands):
    inputs = iter(commands)
    monkeypatch.setattr(
        builtins, "input",
        lambda prompt: next(inputs)
    )
    main()


def test_calculations(monkeypatch, capsys):
    run_cli(monkeypatch, [
        "add 5 3",
        "subtract 10 4",
        "multiply 2 6",
        "divide 10 2",
        "exit",
    ])

    output = capsys.readouterr().out

    assert "8.0" in output
    assert "6.0" in output
    assert "12.0" in output
    assert "5.0" in output
    assert "Goodbye!" in output


def test_history(monkeypatch, capsys):
    run_cli(monkeypatch, [
        "history",
        "add 5 3",
        "history",
        "exit",
    ])

    output = capsys.readouterr().out

    assert "History is empty." in output
    assert "5.0 add 3.0 = 8.0" in output


def test_errors(monkeypatch, capsys):
    run_cli(monkeypatch, [
        "hello",
        "add 5",
        "add 5 3 2",
        "add abc 3",
        "divide 5 0",
        "add 2 3",
        "exit",
    ])

    output = capsys.readouterr().out

    assert "Unknown command." in output
    assert "Please provide exactly two numbers." in output
    assert "Invalid number." in output
    assert "Cannot divide by zero" in output
    assert "5.0" in output


def test_empty_input(monkeypatch, capsys):
    run_cli(monkeypatch, [
        "",
        "   ",
        "exit",
    ])

    output = capsys.readouterr().out
    assert "Goodbye!" in output


def test_history_extra_input(monkeypatch, capsys):
    run_cli(monkeypatch, [
        "history 5",
        "exit",
    ])

    output = capsys.readouterr().out
    assert "History takes no operands." in output


def test_eof(monkeypatch, capsys):
    def raise_eof(prompt):
        raise EOFError

    monkeypatch.setattr(
        builtins, "input",
        raise_eof
    )

    main()

    output = capsys.readouterr().out
    assert "Goodbye!" in output
