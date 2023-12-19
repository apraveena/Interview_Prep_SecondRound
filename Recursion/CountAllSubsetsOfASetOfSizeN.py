#T(n) = O(n)
def count_all_subsets_recursive(n):
    """
    Args:
     n(int32)
    Returns:
     int32
    """
    if n == 0:
        return 1

    return 2 * count_all_subsets(n - 1) # 2 * 2 ** (n-1)

#T(n) = O(n)
def count_all_subsets_iterative(n):
    """
    Args:
     n(int32)
    Returns:
     int32
    """
    result = 1
    for i in range(n):
        result = result * 2
    return result

#T(n) = O(logn)
#recursive divide and conquer
def count_all_subsets(n):
    if n == 0:
        return 1

    sub_result = count_all_subsets(n // 2)
    result = sub_result * sub_result

    if n % 2 != 0:
        result *= 2

    return result

#works but dont necessarily understand this..
def count_all_subsets_iterative_divide_conquer(n):
    result = 1
    multiplier = 2

    while n > 0:
        if n % 2 == 1:
            result = result * multiplier
        n = n // 2
        multiplier = multiplier * multiplier

    return result

print(count_all_subsets_iterative_divide_conquer(3))