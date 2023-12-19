# ik - Largest Connected Component In Binary Square Grid
# Runtime - 3590 ms - Beats 47.83% Memory 27.2 MB Beats 46.74%
class Solution:
    from typing import List
    def largestIsland(self, grid: List[List[int]]) -> int:
        size = len(grid)

        def get_neighbors(row, col):
            results = []
            row_vals = [1, 0, -1, 0]
            col_vals = [0, 1, 0, -1]
            for i in range(len(row_vals)):
                new_row = row + row_vals[i]
                new_col = col + col_vals[i]
                if 0 <= new_row < size and 0 <= new_col < size:
                    results.append((new_row, new_col))

            return results

        def dfs(row, col, component_id):
            grid[row][col] = component_id
            component_size = 1
            for nr, nc in get_neighbors(row, col):
                if grid[nr][nc] == 1:
                    component_size += dfs(nr, nc, component_id)

            return component_size

        component_id = 2
        component_sizes = [0, 0]  # ignore 0 and 1 spots as they are values of grid (land and water)
        for row in range(size):
            for col in range(size):
                if grid[row][col] == 1:
                    comp_size = dfs(row, col, component_id)
                    component_sizes.append(comp_size)
                    component_id += 1


        answer = 0
        zero_val_in_grid = False
        for row in range(size):
            for col in range(size):
                if grid[row][col] == 0:
                    nei_comp_ids = set()
                    zero_val_in_grid = True
                    for nr, nc in get_neighbors(row, col):
                        if grid[nr][nc] != 0:
                            nei_comp_ids.add(grid[nr][nc])
                    curr_size = 1
                    for nei_id in nei_comp_ids:
                        curr_size += component_sizes[nei_id]

                    answer = max(answer, curr_size)

        if not zero_val_in_grid: return size * size
        return answer

sln = Solution()
print(sln.largestIsland([[1,0,1],[0,0,0],[0,1,1]]) == 4)
print(sln.largestIsland([[1,0],[0,1]]) == 3)
print(sln.largestIsland([[1,1],[1,0]]) == 4)




