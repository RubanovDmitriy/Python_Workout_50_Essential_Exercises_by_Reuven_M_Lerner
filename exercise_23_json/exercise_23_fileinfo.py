import os
import glob
import json


def print_scores(dirname):
    result = []
    for filename in glob.glob(f'{dirname}/*'):
        if not os.path.isfile(filename):
            continue
        result.append({'filename': filename,
                       'size': os.stat(filename).st_size,
                       'mtime': os.stat(filename).st_mtime})

    return json.dumps(result)
