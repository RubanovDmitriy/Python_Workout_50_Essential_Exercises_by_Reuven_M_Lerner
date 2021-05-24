def mysum_bigger_than(threshold, *args):
    if not args:
        return args
    output = 0
    for arg in args[1:]:
        if arg > threshold:
            output += arg
    return output
