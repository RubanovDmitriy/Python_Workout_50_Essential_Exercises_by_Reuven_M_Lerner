from io import StringIO
import pytest
# from exercise_4_hexadecimal_output.ex04_hex_output import hex_output


def hex_output():
    hexnum = input('Give me your hex: ')
    print(int(hexnum, 16))


@pytest.mark.parametrize('user_input, output', [
    ('123', '291'),
    ('ff', '255'),
    ('abc123', '11256099')
])
def test_good_input(user_input, output, monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO(user_input + '\n'))
    hex_output()
    captured_out, captured_err = capsys.readouterr()
    assert captured_out.endswith(f'{output}\n')
