def count_islands(matrix):
    """
    Args:
     matrix(list_list_int32)
    Returns:
     int32
    """
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    if not rows or not cols:
        return 0

    number_of_islands = 0

    def get_neighbors(x, y):
        results = []
        row_vals = [0, -1, -1, -1, 0, 1, 1, 1]
        col_vals = [1, 1, 0, -1, -1, -1, 0, 1]

        for k in range(len(row_vals)):
            row_val = x + row_vals[k]
            col_val = y + col_vals[k]
            if row_val >= 0 and row_val < len(matrix) and col_val >= 0 and col_val < len(matrix[0]):
                results.append((row_val, col_val))

        return results

    def dfs(i, j):
        matrix[i][j] = 0
        for (nr, nc) in get_neighbors(i, j):
            if matrix[nr][nc] == 1:
                dfs(nr, nc)

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 1:
                number_of_islands += 1
                dfs(r, c)

    return number_of_islands

# print(count_islands([[1, 1, 0],[1, 1, 0],[0, 0, 0]]) == 1)

from collections import deque

from collections import deque


def count_islands(matrix):
    def count_islands_bfs(row, col):
        q = deque()
        q.append((row, col))
        matrix[row][col] = 0
        while q:
            pos = q.popleft()
            c_row = pos[0]
            c_col = pos[1]
            for (nrow, ncol) in get_neighbors(c_row, c_col):
                if matrix[nrow][ncol] == 1:
                    matrix[nrow][ncol] = 0
                    q.append((nrow, ncol))

    def get_neighbors(x, y):
        results = []
        row_vals = [0, -1, -1, -1, 0, 1, 1, 1]
        col_vals = [1, 1, 0, -1, -1, -1, 0, 1]

        for k in range(len(row_vals)):
            row_val = x + row_vals[k]
            col_val = y + col_vals[k]
            if row_val >= 0 and row_val < len(matrix) and col_val >= 0 and col_val < len(matrix[0]):
                results.append((row_val, col_val))

        return results

        # outer loop

    rows = len(matrix)
    cols = len(matrix[0])
    no_of_islands = 0
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 1:
                no_of_islands = no_of_islands + 1
                count_islands_bfs(row, col)
    return no_of_islands

# print(count_islands1([[1, 1, 0],[1, 1, 0],[0, 0, 0]]) == 1)
print(count_islands([[1],[1]]) == 1)