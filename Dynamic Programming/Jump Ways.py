def jump_ways(n):
    """
    Args:
     n(int32)
    Returns:
     int64
    """
    if n in (1, 2):
        return n

    prev_1, prev_2 = 1, 2

    for i in range(3, n + 1):
        curr = prev_1 + prev_2
        prev_1 = prev_2
        prev_2 = curr

    return curr
