def helper(i, n, k, slate, result):
    if k == len(slate):
        result.append(slate[:])
        return
    if i == n + 1:
        return
    slate.append(i)
    helper(i + 1, n, k, slate, result)
    slate.pop()
    helper(i + 1, n, k, slate, result)

def find_combinations(n, k):
    result = []
    temp = []
    helper(1, n, k, temp, result)
    return result


print(find_combinations(3, 2))