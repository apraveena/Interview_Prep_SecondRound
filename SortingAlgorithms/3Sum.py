def three_sum(a):
    result = []
    a.sort()
    for i, val in enumerate(a):
        if i > 0 and a[i] == a[i-1]:
            continue
        if i == len(a) - 1:
            break
        l = i + 1
        r = len(a) - 1
        while l < r:
            curr_sum = val + a[l] + a[r]
            if curr_sum > 0:
                r -= 1
            elif curr_sum < 0:
                l += 1
            else:
                result.append(f"{val},{a[l]},{a[r]}")
                l += 1
                while a[l] == a[l-1] and l < r:
                    l += 1
    return result

lst1 = [10, 3, -4, 1, -6, 9]
print(three_sum(lst1))