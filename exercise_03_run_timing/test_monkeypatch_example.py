from io import StringIO


def double():
    x = input("Enter an integer: ")
    return int(x) * 2


def adding():
    x = float(input('Enter the first number'))
    y = float(input('Enter the second number'))
    return x + y


def test_double(monkeypatch):
    number_inputs = StringIO('1234\n')
    monkeypatch.setattr('sys.stdin', number_inputs)
    assert double() == 2468


def test_adding(monkeypatch):
    number_inputs = StringIO('2\n3\n')
    monkeypatch.setattr('sys.stdin', number_inputs)
    assert adding() == 5
