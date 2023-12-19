def max_island_size(grid):
    """
    Args:
     grid(list_list_int32)
    Returns:
     int32
    """
    from collections import deque
    global max_area
    max_area = 0

    def get_neighbors(row, col):
        results = []
        row_vals = [0, -1, 0, 1]
        col_vals = [1, 0, -1, 0]
        for i in range(len(row_vals)):
            new_row, new_col = row + row_vals[i], col + col_vals[i]
            if new_row >= 0 and new_row < len(grid) \
                    and new_col >= 0 and new_col < len(grid[0]):
                results.append((new_row, new_col))

        return results

    def bfs(row, col):
        global max_area
        q = deque()
        q.append((row, col))
        grid[row][col] = 0
        curr_max = 0
        while q:
            r, c = q.popleft()
            curr_max += 1
            for nr, nc in get_neighbors(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 0
                    q.append((nr, nc))

        max_area = max(max_area, curr_max)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                bfs(i, j)

    return max_area

print(max_island_size( [
[0, 0, 0],
[0, 0, 0],
[0, 0, 0]
]) == 0)
# print(max_island_size([[1, 1, 0],[1, 1, 0],[0, 0, 1]]) == 4)

