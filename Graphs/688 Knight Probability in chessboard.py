def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):
    """
    Args:
     rows(int32)
     cols(int32)
     start_row(int32)
     start_col(int32)
     end_row(int32)
     end_col(int32)
    Returns:
     int32
    """
    # can also be used for visited flag purposes
    distance = [[-1] * cols for _ in range(rows)]

    def is_valid(row, col):
        return 0 <= row <= len(rows) and 0 <= col < len(cols)

    def get_neighbors(row, col):
        row_vals = [-2, -2, -1, -1, 1, 1, 2, 2]
        col_vals = [1, -1, 2, -2, 2, -2, -1, 1]
        results = []
        for i in range(len(row_vals)):
            new_row = row_vals[i] + row
            new_col = col_vals[i] + col

            if is_valid(new_row, new_col):
                results.append((new_row, new_col))
        return results

    def bfs(row, col):
        from collections import deque
        q = deque()
        q.append((row, col))
        distance[row][col] = 0
        while q:
            row, col = q.popleft()
            for nr, nc in get_neighbors(row, col):
                if distance[nr][nc] == -1:
                    distance[nr][nc] = distance[row][col] + 1
                    if (nr, nc) == (end_row, end_col):
                        return distance[nr][nc]
                    q.append((nr, nc))

        return -1

    return bfs(start_row, start_col)
