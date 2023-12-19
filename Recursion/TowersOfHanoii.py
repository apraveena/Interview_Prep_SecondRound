def tower_of_hanoi_recursive(n):
    """
    Args:
     n(int32)
    Returns:
     list_list_int32
    """
    # Brute Force
    src = 1
    dest = 3
    aux = 2
    temp, result = [], []

    def helper(n, src, dest, aux, temp, result):
        if n == 1:
            temp = []
            temp.append(src)
            temp.append(dest)
            result.append(temp[:])
            return
        helper(n - 1, src, aux, dest, temp, result)
        temp = []
        temp.append(src)
        temp.append(dest)
        result.append(temp[:])
        helper(n - 1, aux, dest, src, temp, result)

    helper(n, src, dest, aux, temp, result)
    return result

print(tower_of_hanoi_recursive(2))