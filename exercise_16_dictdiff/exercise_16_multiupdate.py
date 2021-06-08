def multiupdate(*kwargs):
    result = {}

    for a_dict in kwargs:
        result.update(a_dict)

    return result
