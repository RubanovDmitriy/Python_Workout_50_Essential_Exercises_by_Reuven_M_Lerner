from io import StringIO

import pytest

from exercise_14_restaurant.exercise_14_loginpass import login_pass
from exercise_14_restaurant.exercise_14_restaurant import restaurant


def test_order_nothing(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('\n'))
    restaurant()
    captured_out, captured_err = capsys.readouterr()
    assert captured_out.endswith('Your total is 0\n')


def test_order_one_entree(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('sandwich\n\n'))
    restaurant()
    captured_out, captured_err = capsys.readouterr()
    assert 'sandwich costs 10, total is 10' in captured_out
    assert captured_out.endswith('Your total is 10\n')


def test_order_two_entrees(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('sandwich\nsandwich\n\n'))
    restaurant()
    captured_out, captured_err = capsys.readouterr()
    assert 'sandwich costs 10, total is 10' in captured_out
    assert 'sandwich costs 10, total is 20' in captured_out
    assert captured_out.endswith('Your total is 20\n')


def test_order_many_items(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO(
        'sandwich\nsandwich\nsalad\nelephant\ntea\n\n'))
    restaurant()
    captured_out, captured_err = capsys.readouterr()
    assert 'sandwich costs 10, total is 10' in captured_out
    assert 'sandwich costs 10, total is 20' in captured_out
    assert 'salad costs 9, total is 29' in captured_out
    assert 'elephant isn’t in stock' in captured_out
    assert 'tea costs 7, total is 36' in captured_out
    assert captured_out.endswith('Your total is 36\n')


@pytest.mark.parametrize(('user_input', 'output'), [
    ('Dalanonys@gmail.com\ngBLFZKYzVR', 'You successfully authorized'),
    ('Nevin@gmail.com\n0sX1mYwkQF', 'You successfully authorized'),
    ('Lexilli@gmail.com\nfj2Fh7pHOD', 'You successfully authorized'),
    ('Llintashi@gmail.com\n79Xm2VAnK6', 'You successfully authorized'),
])
def test_correct_login(user_input, output, monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO(user_input + '\n'))
    login_pass()
    captured_out, captured_err = capsys.readouterr()
    assert captured_out.endswith(f'{output}\n')


@pytest.mark.parametrize(('user_input', 'output'), [
    ('Dalanon\n', 'No such login in DataBase'),
    ('Nn@gmail.com\n0sX1mYwkQF', 'No such login in DataBase'),
    ('Lexillail.com\nfj2Fh7pHOD', 'No such login in DataBase'),
    ('@gmail.com\n79Xm2VAnK6', 'No such login in DataBase'),
])
def test_incorrect_login(user_input, output, monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO(user_input + '\n'))
    login_pass()
    captured_out, captured_err = capsys.readouterr()
    assert captured_out.endswith(f'{output}\n')


@pytest.mark.parametrize(('user_input', 'output'), [
    ('Kairlassi@gmail.com\n01AyVKBYX', 'Your password is incorrect'),
    ('Xavonata@gmail.com\nxZEZmjgAz', 'Your password is incorrect'),
    ('Hanevivel@gmail.com\nF6SMbyFnM', 'Your password is incorrect'),
    ('Xenollen@gmail.com\nh6iTD1XnL', 'Your password is incorrect'),
])
def test_incorrect_pass(user_input, output, monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO(user_input + '\n'))
    login_pass()
    captured_out, captured_err = capsys.readouterr()
    assert captured_out.endswith(f'{output}\n')
