import random

import pytest
import string

from exercise_27_pass_gen.exercise_27_pass_gen import create_password_generator


@pytest.mark.parametrize(('pool', 'size', 'pw'), [
    ('abcdef', 8, 'ddaceddc'),
    ('!@#$%', 8, '$$!#%$$#'),
    (string.ascii_lowercase, 20, 'mynbiqpmzjplsgqejeyd')
])
def test_simple(pool, size, pw):
    random.seed(0)
    create_password = create_password_generator(pool)
    output = create_password(size)
    assert len(output) == size
    assert output == pw
