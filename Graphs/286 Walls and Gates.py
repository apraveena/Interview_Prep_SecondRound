class Solution:
    from typing import List
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        inf = 2147483647
        from collections import deque
        q = deque()


        def get_empty_neighbors(row, col):
            row_vals = [1, -1, 0, 0]
            col_vals = [0, 0, 1, -1]
            results = []
            for i in range(len(row_vals)):
                new_row, new_col = row_vals[i] + row, col_vals[i] + col
                if 0 <= new_row < len(rooms) and 0 <= new_col < len(rooms[0]) and rooms[new_row][new_col] == inf:
                    results.append((new_row, new_col))
            return results

        def bfs():
            while q:
                curr_r, curr_c, curr_level = q.popleft()
                for nr, nc in get_empty_neighbors(curr_r, curr_c):
                    if rooms[nr][nc] == inf:
                        rooms[nr][nc] = curr_level + 1
                        q.append((nr, nc, rooms[nr][nc]))

        for row in range(len(rooms)):
            for col in range(len(rooms[0])):
                if rooms[row][col] == 0:
                    q.append((row, col, 0))

        bfs()
        return rooms

sln = Solution()
print(sln.wallsAndGates([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]) == [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]])











