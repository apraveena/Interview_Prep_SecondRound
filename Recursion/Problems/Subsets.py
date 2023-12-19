#leetcode : 78
#powerset
def subsets(arr):
    result = []
    def helper(arr, slate):
        if len(arr) == 0:
            result.append(slate[:])
            return

        helper(arr[1:], slate)

        slate.append(arr[0])
        helper(arr[1:], slate)
        slate.pop()

    helper(arr, [])
    return result

print(subsets([1, 2, 3]))