def find_pascal_triangle(n):
    """
    Args:
     n(int32)
    Returns:
     list_list_int32
    """
    mod = 1000000007
    table = [[] * n for i in range(n)]
    table[0].append(1)

    for row in range(1, n):
        for col in range(0, row + 1):
            if col == 0 or row == col:
                table[row].append(1)
            else:
                table[row].append((table[row - 1][col] + table[row - 1][col - 1]) % mod)
    return table


print(find_pascal_triangle(4))

