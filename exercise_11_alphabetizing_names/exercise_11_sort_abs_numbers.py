def sort_absolute(numbers):
    """Given a sequence of positive and negative numbers, sort them by absolute value."""
    return sorted(numbers, key=abs)
