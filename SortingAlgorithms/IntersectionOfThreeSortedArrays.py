def find_intersection(arr1, arr2, arr3):
    i, j, k = 0, 0, 0
    results = []
    ni, nj, nk = len(arr1), len(arr2), len(arr3)
    while i < ni and j < nj and k < nk:
        if arr1[i] == arr2[j] == arr3[k]:
            results.append(arr1[i])
        min_val = min(arr1[i], arr2[j], arr3[k])

        if min_val == arr1[i]:
            i += 1
        if min_val == arr2[j]:
            j += 1
        if min_val == arr3[k]:
            k += 1

    if len(results) == 0:
        return [-1]
    else:
        return results

arr1 = [2, 5, 10]
arr2 = [2, 3, 4, 10]
arr3 = [2, 4, 10]

# arr1 = [1, 2, 3]
# arr2 = []
# arr3 = [1, 2]

# arr1 = [1, 2, 3]
# arr2 = [3, 4]
# arr3 = [1, 2, 3]

# arr1 = [10, 20]
# arr2 = [10, 20]
# arr3 = [10, 20]

print(find_intersection(arr1, arr2, arr3))

