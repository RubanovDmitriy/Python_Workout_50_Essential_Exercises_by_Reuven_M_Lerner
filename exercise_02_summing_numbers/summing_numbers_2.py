'''So sum([1,2,3], 4) returns 10, because 1+2+3 is 6, which would be added to the starting value of 4. Reim-
plement your mysum function such that it works in this way. If a second argu-
ment is not provided, then it should default to 0. Note that while you can write
a function in Python 3 that defines a parameter after *args , I’d suggest avoid-
ing it and just taking two arguments—a list and an optional starting point.'''


def mysum(numbers, start=0):
    result = start
    for ele in range(0, len(numbers)):
        result = result + numbers[ele]
    return result
