import glob
import json
from statistics import mean


def print_scores(dirname):
    scores = {}

    for filename in glob.glob(f'{dirname}/*'):
        scores[filename] = {}

        with open(filename) as json_file:
            for result in json.load(json_file):
                for subject, score in result.items():
                    scores[filename].setdefault(subject, [])
                    scores[filename][subject].append(score)
            print(scores)

    for one_class in scores:
        print(one_class)
        for subject, score in scores[one_class].items():
            min_value = min(score)
            max_value = max(score)
            average_value = mean(score)
            print(subject)
            print(f'\t min {min_value}')
            print(f'\t max {max_value}')
            print(f'\t average {average_value}')
