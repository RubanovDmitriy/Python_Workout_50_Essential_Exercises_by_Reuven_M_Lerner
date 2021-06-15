import operator


def calc(znak):
    operations = {'+': operator.add,
                  '-': operator.sub,
                  '*': operator.mul,
                  '/': operator.truediv,
                  '**': operator.pow,
                  '%': operator.mod}
    op, first_s, second_s = znak.split()
    first = int(first_s)
    second = int(second_s)

    return operations[op](first, second)
