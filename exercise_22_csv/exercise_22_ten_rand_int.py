import csv
from random import randint
from statistics import mean


def generate_randints():
    rows = []
    for _ in range(10):
        list_line = []
        for _ in range(10):
            list_line.append(randint(1, 100))
        rows.append(list_line)

    return rows


def generate_randint_csv(filename):
    with open(filename, mode='w') as ten_rand_int_file:
        rand_int_writer = csv.writer(ten_rand_int_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for row in generate_randints():
            rand_int_writer.writerow(row)


def read_csv(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            int_row = [int(x) for x in row]
            print(f'Line: {line_count}, Sum: {sum(int_row)}, Mean: {mean(int_row)}')
            line_count += 1
