def mysum(*args):
    if not args:
        return args
    output = args[0]
    for arg in args[1:]:
        output += arg
    return output
