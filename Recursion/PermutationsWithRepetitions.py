def print_decimals(n):
    results = []
    def helper(n, slate):
        if n == 0:
            results.append(slate)
        else:
            for i in range(9, -1, -1):
                helper(n-1, str(i) + slate)
    helper(n, "")

    return results

def permute_array_of_unique_integers_repetitions_allowed(arr):
    results = []
    def helper(arr, slate):
        pass

# print(print_decimals(2))

#I think the following is permutations with repetitions
def permutations(arr):
    res = []
    def helper(slate, a):
        if len(a) == 0:
            res.append(slate[:])
            return

        for i in range(len(a)):
            slate.append(a[i])
            helper(slate, a[:i] + a[i+1: ])
            slate.pop()

    helper([], arr)
    return res

print(permutations([1, 2, 3, 4, 5]))
