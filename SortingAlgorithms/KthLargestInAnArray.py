
def kth_largest_in_an_array_min_heap(numbers, k):
    """
    Args:
     numbers(list_int32)
     k(int32)
    Returns:
     int32
    """
    import heapq
    if len(numbers) == 1:
        return numbers[0]

    heap = numbers[:k]
    n = len(numbers)
    heapq.heapify(heap)
    for i in range(k, n):
        if len(heap) < k:
            heapq.heappush(heap, numbers[i])
        elif numbers[i] > heap[0]:
            heapq.heappushpop(heap, numbers[i])

    return heap[0]

def kth_largest_element_quick_select(arr, k):
    n = len(arr)
    k_idx = n - k

    def helper(l, r):
        p = l
        pivot = arr[r]

        for i in range(l, r):
            if arr[i] < pivot:
                arr[i], arr[p] = arr[p], arr[i]
                p += 1

        arr[p], arr[r] = arr[r], arr[p]

        if p == k_idx:
            return pivot
        elif p > k_idx:
            return helper(l, p-1)
        else:
            return helper(p+1, r)

    result = helper(0, n-1)
    return result

lst1 = [5, 1, 10, 3, 2]
k = 2
# lst1 = [12]
print(kth_largest_element_quick_select(lst1, k))