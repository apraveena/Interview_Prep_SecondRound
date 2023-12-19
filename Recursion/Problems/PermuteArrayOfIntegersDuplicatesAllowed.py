#dont remember if it works..
def get_permutations_v1(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_list_int32
    """
    result = []
    arr.sort()
    def helper(slate, a):
        if len(a) == 0:
            if slate not in result:
                result.append(slate[:])
            return

        # for idx, val in enumerate(a):
        slate.append(a[0])
        helper(slate, a[1:])
        slate.pop()


    for i in range(len(arr)):
        helper([arr[i]], arr[i+1:] + arr[:i])

    return result

#works but some cases time outs
def get_permutations(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_list_int32
    """
    result = []
    arr.sort()
    placed = set()

    def helper(slate, a):
        if len(a) == 0:
            if slate not in result:
                result.append(slate[:])
            return

        for j, val in enumerate(a):
            slate.append(val)
            helper(slate, a[:j] + a[j + 1:])
            slate.pop()

    for i in range(len(arr)):
        if i not in placed:
            placed.add(i)
            helper([arr[i]], arr[:i] + arr[i + 1:])

    return result

#solution by translating java code to python from ik solution
#doesn't work for many cases
def get_permutationsv3(arr):
    result = []
    placed = set()

    def backtrack(fixed_index, slate):
        if fixed_index >= len(arr):
            result.append(slate[:])
            return

        for i in range(fixed_index, len(slate)):
            if not slate[i] in placed:
                placed.add(slate[i])
                slate[fixed_index], slate[i] = slate[i], slate[fixed_index]
                backtrack(fixed_index + 1, slate)
                slate[i], slate[fixed_index] = slate[fixed_index], slate[i]

    backtrack(0, arr)
    return result


#optimal solution - works for all cases - from ik submissions
def get_permutations(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    permutations = []

    def helper(i, slate):
        if i == len(slate) - 1:
            permutations.append(slate[:])
            return

        placed = set()

        for num in range(i, len(slate)):
            if not slate[num] in placed:
                placed.add(slate[num])
                slate[num], slate[i] = slate[i], slate[num]
                helper(i + 1, slate)
                slate[i], slate[num] = slate[num], slate[i]
        return

    helper(0, arr)
    return permutations

print(get_permutations([1, 2, 2]))
print(get_permutations([2, 0, 9]))