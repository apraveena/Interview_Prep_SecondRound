from collections import Counter
def minimumSwap_using_Counter(s1, s2):
    if s1 == s2: return 0
    count = Counter([s1[i] + s2[i] for i in range(len(s1))])
    xy, yx = count['xy'], count['yx']
    return -1 if (xy + yx) % 2 else int(xy/2 + yx/2 + 2*(xy%2))

def minimumSwap(s1: str, s2: str) -> int:
    x_y, y_x = 0, 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if c1 == 'x':
                x_y += 1
            else:
                y_x += 1

    if (x_y + y_x) % 2 == 1:
        return -1
    # Both x_y and y_x count shall either be even or odd to get the result.
    # x_y + y_x should be even

    res = x_y // 2
    res += y_x // 2

    if x_y % 2 == 1:
        res += 2
    # If there count is odd i.e. we have "xy" and "yx" situation
    # so we need 2 more swaps to make them equal

    return res
print(minimumSwap("xx", "yy"))
print(minimumSwap("xy", "yx"))
print(minimumSwap("xx", "xy"))
print(minimumSwap("xxyyxyxyxx", "xyyxyxxxyx"))