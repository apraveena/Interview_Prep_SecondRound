#Time complexity O(mxn) as we are iterating over every node doing constant amount of work
#Space complexity O(mxn) although this can be changed if we only store current and previous row
def unique_paths(n, m):
    """
    Args:
     n(int32)
     m(int32)
    Returns:
     int32
    """
    table = [[0] * (m) for _ in range(n)]
    p = 1000000007

    for i in range(n):
        table[i][0] = 1

    for j in range(m):
        table[0][j] = 1

    for row in range(1, n):
        for col in range(1, m):
            table[row][col] = (table[row - 1][col] + table[row][col - 1]) % p

    return table[n - 1][m - 1]