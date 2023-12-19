def find_fibonacci(n):
    """
    Args:
     n(int32)
    Returns:
     int32
    """
    if n in (1, 0):
        return n

    prev_1, prev_2 = 0, 1
    for i in range(2, n + 1):
        curr = prev_1 + prev_2
        prev_1 = prev_2
        prev_2 = curr

    return curr