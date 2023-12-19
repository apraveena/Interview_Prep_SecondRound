#not passing all test cases
class Solution:
    from typing import List
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        hm = {}
        visited = set()

        def get_neighbors(row, col):
            row_vals = [0, -1, 0, 1]
            col_vals = [-1, 0, 1, 0]
            results = []

            for i in range(len(row_vals)):
                new_row, new_col = row + row_vals[i], col + col_vals[i]
                if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]):
                    results.append((new_row, new_col))
            return results

        def am_i_border_line(row, col):
            return row in (0, len(board) - 1) or col in (0, len(board[0]) - 1)

        def has_path_to_border(r, c):
            visited.add((r, c))
            if am_i_border_line(r, c):
                hm[(r, c)] = True
                return True

            for nr, nc in get_neighbors(r, c):
                if board[nr][nc] == "X":
                    continue

                if (nr, nc) in hm:
                    hm[(r, c)] = True
                    return True

                if (nr, nc) in visited:
                    continue
                is_border = has_path_to_border(nr, nc)
                if is_border:
                    return True

            # board[r][c] = "X"
            return False

        for rr in range(len(board)):
            for cc in range(len(board[0])):
                if board[rr][cc] == "O":
                    ans = has_path_to_border(rr, cc)
                    if not ans:
                        board[rr][cc] = "X"

        return board

sln = Solution()

print(sln.solve([["X","O","X","O","X","O","O","O","X","O"],["X","O","O","X","X","X","O","O","O","X"],["O","O","O","O","O","O","O","O","X","X"],["O","O","O","O","O","O","X","O","O","X"],["O","O","X","X","O","X","X","O","O","O"],["X","O","O","X","X","X","O","X","X","O"],["X","O","X","O","O","X","X","O","X","O"],["X","X","O","X","X","O","X","O","O","X"],["O","O","O","O","X","O","X","O","X","O"],["X","X","O","X","X","X","X","O","O","O"]]))
# print(sln.solve([["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]))
# print(sln.solve([["O","O","O"],["O","O","O"],["O","O","O"]]) == [["O","O","O"],["O","O","O"],["O","O","O"]])

#output
[["X","O","X","O","X","O","O","O","X","O"],["X","O","O","X","X","X","O","O","O","X"],["O","O","O","O","O","O","O","O","X","X"],["O","O","O","O","O","O","X","O","O","X"],["O","O","X","X","O","X","X","O","O","O"],["X","O","O","X","X","X","X","X","X","O"],["X","O","X","X","X","X","X","O","X","O"],["X","X","O","X","X","X","X","X","X","X"],["O","O","O","O","X","X","X","O","X","O"],["X","X","O","X","X","X","X","O","O","O"]]
[["X","O","X","O","X","O","O","O","X","O"],["X","O","O","X","X","X","O","O","O","X"],["O","O","O","O","O","O","O","O","X","X"],["O","O","O","O","O","O","X","O","O","X"],["O","O","X","X","O","X","X","O","O","O"],["X","O","O","X","X","X","X","X","X","O"],["X","O","X","X","X","X","X","O","X","O"],["X","X","O","X","X","X","X","O","O","X"],["O","O","O","O","X","X","X","O","X","O"],["X","X","O","X","X","X","X","O","O","O"]]
#expected


