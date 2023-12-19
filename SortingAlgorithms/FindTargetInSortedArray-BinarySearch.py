def helper(arr, start, end, target):
    if start == end:
        return arr[start] == target

    mid = (end-start)//2 + start
    if arr[mid] > target:
        return helper(arr, start, mid-1, target)
    elif arr[mid] < target:
        return helper(arr, mid + 1, end, target)
    else:
        return True

def find_target_in_sorted_array_recursive(arr, target):
    return helper(arr, 0, len(arr)-1, target)

def find_target_in_sorted_array_iterative(arr, target):
    while start <= end:
        mid = (end - start) // 2
        if target > arr[mid]:
            start = mid + 1
        elif target < arr[mid]:
            end = mid - 1
        else:
            return True
    return False

print(find_target_in_sorted_array_recursive([3, 5, 8], 7))