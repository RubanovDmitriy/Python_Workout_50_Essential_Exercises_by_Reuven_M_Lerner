from collections import defaultdict


def shells_users(filename):
    output = defaultdict(list)

    for one_line in open(filename):
        if one_line.startswith(('#', '\n')):
            continue
        username, *ignore, shell = one_line.strip().split(':')
        output[shell].append(username)
    return output
