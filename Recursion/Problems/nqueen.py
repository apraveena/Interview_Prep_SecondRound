#leetcode: 51
def nqueen(n):
    result = []
    def is_conflict(arr):
        if len(arr) < 2:
            return False
        recent_queen_idx = len(arr)-1
        for q in range(recent_queen_idx):
            if abs(arr[recent_queen_idx] - arr[q]) == 0:
                return True
            no_of_rows_between = recent_queen_idx-q
            no_of_cols_between = arr[recent_queen_idx] - arr[q]
            if abs(no_of_rows_between) == abs(no_of_cols_between):
                return True
        return False

    def format_results(arr, n):
        result = []

        for item in arr:
            temp = []
            for idx, elem in enumerate(item):
                row = ["-"] * n
                row[elem] = "q"
                temp.append("".join(row))
            result.append(temp)
        return result

    def helper(slate):
        if is_conflict(slate):
            return
        if len(slate) == n:
            result.append(slate[:])
            return

        for q in range(n):
            slate.append(q)
            helper(slate)
            slate.pop()

    helper([])
    return format_results(result, n)

print(nqueen(5))