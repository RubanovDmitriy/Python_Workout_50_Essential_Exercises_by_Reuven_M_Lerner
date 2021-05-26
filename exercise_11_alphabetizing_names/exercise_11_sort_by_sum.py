def sort_by_sum(list_of_lists):
    """Given a list of lists, with each list containing zero or more numbers, sort by the
    sum of each inner list’s numbers."""
    return sorted(list_of_lists, key=sum)

print(sort_by_sum([
    [1, 3, 99],
    [4, 8, 1, 44],
    [999, 5, 77]
]))
