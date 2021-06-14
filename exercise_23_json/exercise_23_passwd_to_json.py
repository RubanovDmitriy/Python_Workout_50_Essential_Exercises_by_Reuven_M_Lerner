import json


def passwd_to_json(filename):
    passwords = []
    with open(filename) as passwd:

        for line in passwd:
            if not line.startswith(('#', '\n')):
                passwords.append(tuple(line.split(':')))
    return json.dumps(passwords)
