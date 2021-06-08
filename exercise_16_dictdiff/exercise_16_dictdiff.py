def dictdiff(first, second):
    result = {}
    all_keys = first.keys() & second.keys()

    for key in all_keys:
        if first.get(key) != second.get(key):
            result[key] = [first.get(key), second.get(key)]

    return result
