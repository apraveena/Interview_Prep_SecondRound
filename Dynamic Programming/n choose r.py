def ncr(n, r):
    """
    Args:
     n(int32)
     r(int32)
    Returns:
     int32
    """
    p = 1000000007

    if n < r:
        return 0

    if r in (0, 1):
        return 1

    temp = [[0] * (r + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        temp[i][0] = 1

    for i in range(1, r + 1):
        temp[i][i] = 1

    for i in range(2, n + 1):
        for j in range(1, min(r + 1, i + 1)):
            temp[i][j] = temp[i - 1][j] + temp[i - 1][j - 1]

    return temp[n][r] % p

def ncr1(n, r):
    """
    Args:
     n(int32)
     r(int32)
    Returns:
     int32
    """
    # Write your code here.
    if n < r:
        return 0
    if r == 0 or r == n:
        return 1
    table = [[0 for i in range(r + 1)] for j in range(n + 1)]
    for row in range(0, n + 1):
        table[row][0] = 1
    for col in range(1, r):
        # digonal combination of (k,k)
        table[col][col] = 1
    for row in range(2, n + 1):
        for col in range(1, min(r, row) + 1):
            table[row][col] = table[row - 1][col] + table[row - 1][col - 1]
    return table[n][r]


def ncr_test(n, r):
    """
    Args:
     n(int32)
     r(int32)
    Returns:
     int32
    """
    p = 1000000007

    if n < r:
        return 0

    # if r in (0, 1):
    #     return 1

    temp = [[0] * (r + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        temp[i][0] = 1

    for i in range(1, r + 1):
        temp[i][i] = 1

    for row in range(2, n + 1):
        for j in range(1, min(r + 1, row)):
            temp[row][j] = (temp[row - 1][j] + temp[row - 1][j - 1]) % p

    return temp[n][r]


print(ncr_test(10, 9) == 10)
print(ncr_test(10, 8))
print(ncr_test(10, 10) == 1)
print(ncr_test(5, 3) == 10)