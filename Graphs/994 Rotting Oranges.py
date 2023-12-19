class Solution:
    from typing import List
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        """
        Args:
        grid(list_list_int32)
        Returns:
        int32
        """
        result = 0

        def get_neighbors(row, col):
            row_vals = [1, -1, 0, 0]
            col_vals = [0, 0, 1, -1]
            results = []
            for i in range(len(row_vals)):
                new_row, new_col = row + row_vals[i], col + col_vals[i]
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                    results.append((new_row, new_col))
            return results

        q = deque()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    q.append((row, col))

        while q:
            result += 1
            for i in range(len(q)):
                curr_row, curr_col = q.popleft()
                for nr, nc in get_neighbors(curr_row, curr_col):
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return -1

        # if the result = 0, then it means, there were no fresh oranges to begin with
        return max(0, result - 1)

sln = Solution()
print(sln.rotting_oranges([
[2, 1, 1],
[1, 0, 0],
[1, 1, 0]
]) == 3)