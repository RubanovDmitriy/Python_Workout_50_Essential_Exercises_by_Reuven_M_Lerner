import numpy


def factorial(*args):
    result = []
    for _ in args:
        result.append(_)
    return numpy.prod(result)
