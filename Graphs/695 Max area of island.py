class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        global max_island, curr_max
        max_island, curr_max = 0, 0

        def get_neighbors(row, col):
            row_vals = [0, -1, 0, 1]
            col_vals = [1, 0, -1, 0]
            results = []
            for i in range(len(row_vals)):
                new_row, new_col = row + row_vals[i], col + col_vals[i]
                if new_row >= 0 and new_row < len(grid) and new_col >= 0 and \
                        new_col < len(grid[0]):
                    results.append((new_row, new_col))

            return results

        def bfs(row, col):
            global max_island, curr_max
            q = deque()
            q.append((row, col))
            grid[row][col] = 0
            while q:
                r, c = q.popleft()
                curr_max += 1
                for nr, nc in get_neighbors(r, c):
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        q.append((nr, nc))
            max_island = max(max_island, curr_max)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    curr_max = 0
                    bfs(i, j)

        return max_island
