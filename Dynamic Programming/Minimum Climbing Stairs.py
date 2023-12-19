# Time complexity = O(n)
# Space complexity = O(n)
def min_cost_climbing_stairs(cost):
    """
    Args:
     cost(list_int32)
    Returns:
     int32
    """
    n = len(cost)
    # 2 more extra spaces for floor step and destination step
    table = [0] * (n + 2)
    cost.append(0)  # for destination step, helps avoiding an error with code below

    table[0] = 0
    table[1] = cost[0]

    for i in range(2, n + 2):
        table[i] = cost[i - 1] + min(table[i - 1], table[i - 2])

    return table[n + 1]
