def even_odd_dicts(args):
    print(args)
    if len(args) % 2:
        raise ValueError('Need an even number of args')

    output = {}

    while args:
        output[args[0]] = args[1]
        args = args[2:]

    return output
