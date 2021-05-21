def myzip(*args):
    return [tuple(a[i] for a in args)
            for i in range(len(min(args, key=len)))]
