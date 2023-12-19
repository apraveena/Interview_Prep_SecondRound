class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        global result
        result = 0

        def get_water_neighbor_count(row, col):
            row_vals = [-1, 1, 0, 0]
            col_vals = [0, 0, -1, 1]
            nei_size = 0
            if row == 0:
                nei_size += 1
            if row == len(grid) - 1:
                nei_size += 1
            if col == 0:
                nei_size += 1
            if col == len(grid[0]) - 1:
                nei_size += 1

            for i in range(len(row_vals)):
                new_row = row + row_vals[i]
                new_col = col + col_vals[i]
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 0:
                    nei_size += 1

            return nei_size

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    result += get_water_neighbor_count(row, col)

        return result

