import glob
import hashlib


def hash_file(directory):
    result = {}

    for file in glob.glob(f'{directory}/*'):
        h = hashlib.md5()
        h.update(file.encode())
        result[file] = h
    return result
