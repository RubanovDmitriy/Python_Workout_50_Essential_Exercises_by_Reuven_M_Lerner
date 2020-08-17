import pytest

'''Write a function that takes a float and two integers ( before and after ). The
function should return a float consisting of before digits before the decimal
point and after digits after. Thus, if we call the function with 1234.5678 , 2 and
3 , the return value should be 34.567'''


def divider(number: float,
            before: int,
            after: int):

    result = 0

    return print(number, before, after)


divider(1234.1234, 2, 3)


def test_divider():
    assert divider(1234.5678, 2, 3) == 34.567

