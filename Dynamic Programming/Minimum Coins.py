
def minimum_coins(coins, value):
    """
    Args:
     coins(list_int32)
     value(int32)
    Returns:
     int32
    """
    import math

    table = [math.inf] * (value + 1)
    table[0] = 0
    for i in range(1, value + 1):
        for idx, coin in enumerate(coins):
            if i - coin >= 0:
                table[i] = min(table[i], table[i - coin])
        table[i] += 1

    return table[value]

print(minimum_coins([1, 3, 5], 9) == 3)
print(minimum_coins([1, 2, 7], 13) == 4)