import os


def different_extensions(dirname):
    print(os.listdir(dirname))
    return {os.path.splitext(one_filename)[-1]
            for one_filename in os.listdir(dirname)}
