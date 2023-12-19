
def solve_sudoku_puzzle_my_try(board):
    """
    Args:
     board(list_list_int32)
    Returns:
     list_list_int32
    """
    poss_map = {}

    def find_curr_number(row_idx, col_idx):
        poss_nums = []
        row = board[row_idx]

        #find all the possible numbers in the row by eliminating the numbers that are already in the row
        for i in range(9):
            if i + 1 not in row:
                poss_nums.append(i + 1)
        # find all the possible numbers in the column by eliminating the numbers that are already in the column
        for i in range(9):
            if (i + 1) != board[i][col_idx] and i + 1 not in poss_nums:
                poss_nums.append(i + 1)
            if i + 1 == board[i][col_idx] and i + 1 in poss_nums:
                poss_nums.remove(i + 1)


        if len(poss_nums) == 1:
            board[row_idx][col_idx] = poss_nums[0]
        else:
            poss_map[(row_idx, col_idx)] = poss_nums

    def helper():
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    # find the number that belongs here
                    find_curr_number(i, j)

    helper()
    return board

#from ik
def solve_sudoku_puzzle(board):

    def is_safe(r_idx, c_idx, num):
        for i in range(9):
            if board[r_idx][i] == num:
                return False

        for i in range(9):
            if board[i][c_idx] == num:
                return False

        r_start, c_start = r_idx - r_idx % 3, c_idx - c_idx % 3
        for i in range(r_start, r_start + 3):
            for j in range(c_start, c_start + 3):
                if board[i][j] == num:
                    return False

        return True

    def backtrack_helper():
        empty_cell_found = False
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == 0:
                    empty_cell_found = True
                    break
            if empty_cell_found:
                break
        if not empty_cell_found:
            return True

        for i in range(1, 10):
            if is_safe(row, col, i):
                board[row][col] = i
                if backtrack_helper():
                    return True
                else:
                    board[row][col] = 0

        return False

    backtrack_helper()
    return board


board =  [
[8, 4, 9, 0, 0, 3, 5, 7, 0],
[0, 1, 0, 0, 0, 0, 0, 0, 0],
[7, 0, 0, 0, 9, 0, 0, 8, 3],
[0, 0, 0, 9, 4, 6, 7, 0, 0],
[0, 8, 0, 0, 5, 0, 0, 4, 0],
[0, 0, 6, 8, 7, 2, 0, 0, 0],
[5, 7, 0, 0, 1, 0, 0, 0, 4],
[0, 0, 0, 0, 0, 0, 0, 1, 0],
[0, 2, 1, 7, 0, 0, 8, 6, 5]
]
print(board)
print(solve_sudoku_puzzle(board))