import operator


def calc(to_calc):
    operations = {'+': operator.add,
                  '-': operator.sub,
                  '*': operator.mul,
                  '/': operator.truediv,
                  '**': operator.pow,
                  '%': operator.mod}
    op, *numbers = to_calc.split()

    output = int(numbers[0])
    for one_number in numbers[1:]:
        output = operations[op](output, int(one_number))
        print(output)

    return output
