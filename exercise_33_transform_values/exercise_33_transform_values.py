def transform_values(func, indict):
    return {key: func(value) for key, value in indict.items()}
