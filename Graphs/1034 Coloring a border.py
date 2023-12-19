class Solution:
    from typing import List
    def colorBorder(self, grid: List[List[int]], src_row: int, src_col: int, color: int) -> List[List[int]]:
        global visited
        if not grid:
            return grid

        visited = set()
        #temporarily changing to a different color
        new_color = -1

        def get_neighbors(x, y):
            row_vals = [0, -1, 0, 1]
            col_vals = [1, 0, -1, 0]
            results = []
            for i in range(len(row_vals)):
                new_row, new_col = x + row_vals[i], y + col_vals[i]
                if new_row >= 0 and new_row < len(grid) \
                        and new_col >= 0 and new_col < len(grid[0]) :
                    results.append((new_row, new_col))
            return results

        def is_border_old_color(row, col):
            nei = get_neighbors(row, col)
            if len(nei) != 4:
                return False
            return all(grid[r][c] in (old_color, -1) for r, c in nei)

        def bfs(row, col):
            from collections import deque
            global visited
            q = deque()
            q.append((row, col))
            grid[row][col] = old_color if is_border_old_color(src_row, src_col) else new_color
            visited.add((row, col))
            while q:
                row, col = q.popleft()
                for nr, nc in get_neighbors(row, col):
                    if grid[nr][nc] == old_color and (nr, nc) not in visited:
                        if not is_border_old_color(nr, nc):
                            grid[nr][nc] = new_color
                        visited.add((nr, nc))
                        q.append((nr, nc))

        old_color = grid[src_row][src_col]
        bfs(src_row, src_col)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == new_color:
                    grid[i][j] = color


        return grid
sln = Solution()
print(sln.colorBorder([[1,1,1],[1,1,1],[1,1,1]], 1, 1, 2) == [[2,2,2],[2,1,2],[2,2,2]])
print(sln.colorBorder([[1,2,1,2,1,2],[2,2,2,2,1,2],[1,2,2,2,1,2]], 1, 3, 1) == [[1,1,1,1,1,2],[1,2,1,1,1,2],[1,1,1,1,1,2]])
print(sln.colorBorder([[1,2,1,2,1,2],[2,2,2,2,1,2],[1,2,2,2,1,2]], 1, 3, 1) == [[1,1,1,1,1,2],[1,2,1,1,1,2],[1,1,1,1,1,2]])


