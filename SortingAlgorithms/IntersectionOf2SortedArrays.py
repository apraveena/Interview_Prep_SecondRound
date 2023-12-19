def intersection_of_sorted_arrays(arr1, arr2):
    idx1, idx2 = 0, 0
    result = []
    while idx1 < len(arr1) and idx2 < len(arr2):
        if arr1[idx1] < arr2[idx2]:
            idx1 += 1
        elif arr1[idx1] > arr2[idx2]:
            idx2 += 1
        else:
            result.append(idx1)
            idx1 += 1
            idx2 += 1
    return result
lst1 = [2, 6, 7, 8]
lst2 = [6, 8]
print(intersection_of_sorted_arrays(lst1, lst2))