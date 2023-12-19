def check_if_sum_possible(arr, k):
    """
    Args:
     arr(list_int64)
     k(int64)
    Returns:
     bool
    """

    def helper(sub_sum, n, i):
        if sub_sum == k:
            return True

        if n == 0:
            return False

        #Inclusion
        res = helper(sub_sum + arr[i], n-1, i+1)
        if res: return True
        #Exclusion
        res = helper(sub_sum, n-1, i+1)
        if res: return True
        # exhausted all combinations, didn't return
        return False

    return helper(0, len(arr), 0)


print(check_if_sum_possible([1], 0))
print(check_if_sum_possible([2, 14, 7], 6))
print(check_if_sum_possible([2, 4, 7], 6))