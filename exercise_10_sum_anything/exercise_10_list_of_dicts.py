def list_of_dicts(*args):
    output = {}

    for d in args:
        for key, value in d.items():
            if key in output:
                try:
                    output[key].append(value)
                except AttributeError:
                    output[key] = [output[key], value]
            else:
                output[key] = value

    return output
