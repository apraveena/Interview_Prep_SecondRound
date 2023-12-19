def count_triplets(target, a):
    """
    Args:
     target(int32)
     numbers(list_int32)
    Returns:
     int32
    """

    a.sort()
    n = len(a)
    result = 0
    for i in range(0, n-2):
        l, r = i + 1, n - 1
        while l < r:
            temp_sum = a[i] + a[l] + a[r]
            if temp_sum < target:
                # since we found the combo that works,
                # all the numbers to the left of r till l
                # will also work.. just include those numbers
                result += r - l
                # try a new combination
                l += 1
            else:
                r -= 1
    return result

lst1 = [-1, 3, 5, 7, 9, 11]
target = 12 #Expected answer = 4
lst1 =  [3, 1, 234, 131, 0, 0, 0, 1]
target = 10 #Expected answer = 20
print(count_triplets(target, lst1))