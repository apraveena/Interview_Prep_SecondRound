class Solution:
    from typing import List

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        from collections import deque
        n, pos = len(board), 0
        max_square = n * n
        visited = {}

        if not n:
            return 0

        def get_rowcol_from_pos(pos):
            row = (pos - 1) // n
            if row % 2 == 0:
                col = (pos - 1) % n
            else:
                col = (n - 1) - ((pos - 1) % n)
            row = n - row - 1
            return (row, col)

        def bfs(node):
            q = deque()
            q.append(node)
            visited[node] = 0
            while q:
                curr = q.popleft()
                for i in range(1, 7):
                    next_pos = curr + i
                    if next_pos > max_square:
                        continue
                    (r, c) = get_rowcol_from_pos(next_pos)
                    if board[r][c] != -1:
                        next_pos = board[r][c]
                    if next_pos not in visited:
                        q.append(next_pos)
                        visited[next_pos] = visited[curr] + 1
                        if next_pos == max_square:
                            return visited[next_pos]

            return -1

        return bfs(1)

sln = Solution()
# print(sln.snakesAndLadders([[-1,-1],[-1,3]]) == 1)
# print(sln.snakesAndLadders([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]) == 4)
print(sln.snakesAndLadders([[-1,-1,19,10,-1],[2,-1,-1,6,-1],[-1,17,-1,19,-1],[25,-1,20,-1,-1],[-1,-1,-1,-1,15]]) == 2)


