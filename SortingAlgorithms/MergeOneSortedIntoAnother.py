def merge_one_into_another(first, second):
    """
    Args:
     first(list_int32)
     second(list_int32)
    Returns:
     list_int32
    """
    n = len(first)
    pt1, pt2, final = n - 1, n - 1, 2 * n - 1
    while pt1 >= 0 and pt2 >= 0:
        if first[pt1] > second[pt2]:
            second[final] = first[pt1]
            pt1 -= 1
            final -= 1
        else:
            second[final] = second[pt2]
            pt2 -= 1
            final -= 1

    while pt1 >= 0:
        second[final] = first[pt1]
        pt1 -= 1
        final -= 1

    while pt2 >= 0:
        second[final] = second[pt2]
        pt2 -= 1
        final -= 1

    return second

first = [1, 3, 5]
second =  [2, 4, 6, 0, 0, 0]
print(merge_one_into_another(first, second))