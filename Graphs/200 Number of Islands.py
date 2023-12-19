#289 ms
class Solution:
    from typing import List
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque

        if not len(grid) or not len(grid[0]):
            return 0

        def get_neighbors(x, y):
            results = []
            if x + 1 < len(grid):
                results.append((x + 1, y))
            if y + 1 < len(grid[0]):
                results.append((x, y + 1))
            if x - 1 >= 0:
                results.append((x - 1, y))
            if y - 1 >= 0:
                results.append((x, y - 1))
            return results

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = 0
            while q:
                row, col = q.popleft()
                for nei_r, nei_c in get_neighbors(row, col):
                    if grid[nei_r][nei_c] == "1":
                        grid[nei_r][nei_c] = "0"
                        q.append((nei_r, nei_c))

        no_of_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    no_of_islands += 1
                    bfs(i, j)

        return no_of_islands

#using dfs - 292 ms
class Solution1:
    from typing import List
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque

        if not len(grid) or not len(grid[0]):
            return 0

        def get_neighbors(x, y):
            results = []
            if x + 1 < len(grid):
                results.append((x + 1, y))
            if y + 1 < len(grid[0]):
                results.append((x, y + 1))
            if x - 1 >= 0:
                results.append((x - 1, y))
            if y - 1 >= 0:
                results.append((x, y - 1))
            return results

        def dfs(r, c):
            grid[r][c] = "0"
            for nei_r, nei_c in get_neighbors(r, c):
                if grid[nei_r][nei_c] == "1":
                    dfs(nei_r, nei_c)

        no_of_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    no_of_islands += 1
                    dfs(i, j)

        return no_of_islands


sln = Solution()
print(sln.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]) == 1)
print(sln.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]) == 3)
print(sln.numIslands([["1","0","1","1","0","1","1"]]) == 3)