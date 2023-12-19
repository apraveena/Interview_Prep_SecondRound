def maximum_stolen_value(values):
    """
    Args:
     values(list_int32)
    Returns:
     int32
    """
    memo = [-1] * (len(values) + 1)
    memo[0] = 0
    memo[1] = values[0]

    def rob(i):
        if memo[i] != -1:
            return memo[i]

        memo[i] = max(rob(i - 1), values[i - 1] + rob(i - 2))
        return memo[i]

    return rob(len(values))


print(maximum_stolen_value([6, 1, 2, 7]) == 13)
print(maximum_stolen_value([1,2,3,1]) == 4)