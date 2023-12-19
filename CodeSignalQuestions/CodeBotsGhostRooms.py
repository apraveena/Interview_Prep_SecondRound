'''
https://app.codesignal.com/arcade/intro/level-2/xskq4ZxLyqQMCLshr/solutions
After becoming famous, the CodeBots decided to move into a new building together. Each of the rooms has a different cost, and some of them are free, but there's a rumour that all the free rooms are haunted! Since the CodeBots are quite superstitious, they refuse to stay in any of the free rooms, or any of the rooms below any of the free rooms.

Given matrix, a rectangular matrix of integers, where each value represents the cost of the room, your task is to return the total sum of all rooms that are suitable for the CodeBots (ie: add up all the values that don't appear below a 0).

Example

For

matrix = [[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]
the output should be
solution(matrix) = 9.
There are several haunted rooms, so we'll disregard them as well as any rooms beneath them. Thus, the answer is 1 + 5 + 1 + 2 = 9.

For

matrix = [[1, 1, 1, 0],
          [0, 5, 0, 1],
          [2, 1, 3, 10]]
the output should be
solution(matrix) = 9.
Note that the free room in the final column makes the full column unsuitable for bots (not just the room directly beneath it).
Thus, the answer is 1 + 1 + 1 + 5 + 1 = 9.

'''
def solution(matrix):
    final_sum = 0
    row_count = len(matrix)
    col_count = len(matrix[0])
    for i in range(row_count):
        for j in range(col_count):
            skip_this = False
            if matrix[i][j] == 0:
                continue
            if i > 0:
                for k in range(0, i):
                    if matrix[k][j] == 0:
                        skip_this = True
                        break
            if skip_this:
                continue
            final_sum += matrix[i][j]
    return final_sum

def better_solution(matrix):
    return_val = 0
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            if matrix[i][j] == 0: break
            else: return_val += matrix[i][j]
    return return_val