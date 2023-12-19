def merge(arr, start, mid, end):
    low1 = start
    low2 = mid + 1
    temp = []
    while low1 <= mid and low2 <= end:
        if arr[low1] < arr[low2]:
            temp.append(arr[low1])
            low1 += 1
        else:
            temp.append(arr[low2])
            low2 += 1

    while low1 <= mid:
        temp.append(arr[low1])
        low1 += 1

    while low2 <= end:
        temp.append(arr[low2])
        low2 += 1

    arr[start: end + 1] = temp[:]
    return arr


def helper(arr, start, end):
    if start == end:
        return
    mid = start + (end - start) // 2
    helper(arr, start, mid)
    helper(arr, mid + 1, end)
    return merge(arr, start, mid, end)


def merge_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    n = len(arr)
    if n <= 1: return arr
    helper(arr, 0, n - 1)
    return arr

print(merge_sort([45,2, 5,6, 7 ,73, 33, 21]))