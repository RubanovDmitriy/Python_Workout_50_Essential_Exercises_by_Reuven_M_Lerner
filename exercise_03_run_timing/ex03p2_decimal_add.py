from decimal import Decimal


def decimal_add(first: str, last: str) -> float:
    return float(Decimal(first) + Decimal(last))
