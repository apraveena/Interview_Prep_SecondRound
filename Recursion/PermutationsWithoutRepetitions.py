def permutations_for_string(s):
    result = []
    def helper(slate, arr):
        if len(arr) == 0:
            print(slate)
            return

        for idx, ltr in enumerate(arr):
            helper(ltr + slate, arr[:idx] + arr[idx + 1:])

    helper("", s)

def permutations_for_string_result(s):
    result = []
    def helper(slate, arr):
        if len(arr) == 0:
            result.append(slate)
            return

        for idx, ltr in enumerate(arr):
            helper(ltr + slate, arr[:idx] + arr[idx + 1:])

    helper("", s)
    return result

def permute_array_of_unique_integers(arr):
    result, slate = [], []
    def helper(slate, arr):
        if len(arr) == 0:
            result.append(slate[:])
            return

        for idx, item in enumerate(arr):
            slate.append(item)
            helper(slate, arr[:idx] + arr[idx+1:])
            slate.pop()

    helper([], arr)
    return result

arr =  [1, 2, 3]
print(permute_array_of_unique_integers(arr))


