from collections import Counter


def status_codes_counter(filename):
    status_codes_count = []

    for line in open(filename):
        status_codes_count.append(line.split()[8])

    return Counter(status_codes_count)
