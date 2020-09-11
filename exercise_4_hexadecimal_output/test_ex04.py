from io import StringIO
from exercise_4_hexadecimal_output.ex04_hex_output import hex_output

# def hex_output():
#     hexnum = input('Give me your hex: ')
#     return int(hexnum, 16)


def test_ex04_hex_output(monkeypatch):
    hex_input = StringIO('0x4d2\n')
    monkeypatch.setattr('sys.stdin', hex_input)
    assert hex_output() == 1234
