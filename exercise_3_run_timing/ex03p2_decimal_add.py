from decimal import *


def decimal_add(first: str, last: str) -> float:
    result = float(Decimal(first) + Decimal(last))
    return result


decimal_add('1.2', '1.3')
