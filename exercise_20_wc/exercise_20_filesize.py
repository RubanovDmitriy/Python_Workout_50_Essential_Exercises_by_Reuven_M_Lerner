import glob
import os


def file_sizes(dirname):
    result = {}
    for filename in glob.glob(f'{dirname}/*'):
        if os.path.isfile(filename):
            result[filename] = os.stat(filename).st_size

    return result
