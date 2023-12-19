#Time complexity O(mxn) as we are iterating over every node doing constant amount of work
#Space complexity O(mxn) although this can be better if we use the original grid to store the sum

def maximum_path_sum(grid):
    """
    Args:
     grid(list_list_int32)
    Returns:
     int32
    """
    # m number of rows
    m = len(grid)
    # n is number of columns
    n = len(grid[0])
    table = [[0] * n for _ in range(m)]
    table[0][0] = grid[0][0]
    for i in range(1, m):
        table[i][0] = grid[i][0] + table[i - 1][0]
    for j in range(1, n):
        table[0][j] = grid[0][j] + table[0][j - 1]

    for row in range(1, m):
        for col in range(1, n):
            table[row][col] = grid[row][col] + max(table[row - 1][col], table[row][col - 1])

    return table[m - 1][n - 1]

#Time complexity O(mxn) as we are iterating over every node doing constant amount of work
#Space complexity O(1) since we are using the input grid
def maximum_path_sum_better_space_complexity(grid):
    """
    Args:
     grid(list_list_int32)
    Returns:
     int32
    """
    # m = number of rows, n = number of columns
    m, n = len(grid), len(grid[0])

    for i in range(1, m):
        grid[i][0] = grid[i][0] + grid[i - 1][0]
    for j in range(1, n):
        grid[0][j] = grid[0][j] + grid[0][j - 1]

    for row in range(1, m):
        for col in range(1, n):
            grid[row][col] = grid[row][col] + max(grid[row - 1][col], grid[row][col - 1])

    return grid[m - 1][n - 1]

print(maximum_path_sum([[1, -4, 3], [4, -2, 2]]) == 5)
print(maximum_path_sum([[4, 5, 8], [3, 6, 4], [2, 4, 7]]) == 28)