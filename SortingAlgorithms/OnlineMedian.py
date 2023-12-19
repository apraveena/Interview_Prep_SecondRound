import heapq

def online_median_brute_force(stream):
    """
    Args:
     stream(list_int32)
    Returns:
     list_int32
    """
    # Brute Force
    result = []
    def helper(arr, start, end):
        arr = stream[start:end]
        arr.sort()
        n = len(arr)
        mid = start + (end - start) // 2
        if n == 2:
            result.append((arr[0] + arr[1])//2)
        elif n % 2 == 0:
            mid1 = mid - 1
            result.append((arr[mid] + arr[mid1]) // 2)
        else:
            result.append(arr[mid])

    for i in range(len(stream)):
        helper(stream[:i + 1], 0, i+1)

    return result

#Doesn't work
def online_median_heapify1(stream):
    import heapq
    result = []
    # k = 1
    heap = []
    for i in range(len(stream)):
        heapq.heappush(heap, stream[i])
        mid = (i // 2) + 1
        if len(heap) == 1:
            result.append(stream[0])
        elif len(heap) % 2 == 0: #if even number
            result.append((stream[mid] + stream[mid-1]) // 2)
        else:
            result.append(mid)
        # k += 1
    return result

#Neatcode solution - https://www.youtube.com/watch?v=itmhHWaHupI
#Since Python only provides minheap. We multiply the values with -1 to convert that to max heap
#small is max heap, large is min heap
def add_number(num, small, large):
    heapq.heappush(small, -num)
    if small and large and -small[0] > large[0]:
        val = -heapq.heappop(small)
        heapq.heappush(large, val)

    if len(small) > len(large) + 1:
        val = -heapq.heappop(small)
        heapq.heappush(large, val)

    if len(large) > len(small) + 1:
        val = -heapq.heappop(large)
        heapq.heappush(small, val)

#If we have odd number of items, then take small element from max heap
def find_median(small, large):
    if len(small) == len(large):
        return (-small[0] + large[0])//2
    elif len(small) > len(large):
        return -small[0]
    else:
        return large[0]

 #Maintain 2 arrays max heap and min heap
def online_median_heapify(arr):
    small_heap, large_heap = [], [] #small is max heap, large is min heap
    result = []
    for item in arr:
        add_number(item, small_heap, large_heap)
        result.append(find_median(small_heap, large_heap))

    return result

# lst1 = [3, 8, 5, 2]

#third time
#Python only provides min heap
def online_median_again(stream):
    import heapq
    small_max_heap, large_min_heap, result = [], [], []
    def add_num(num):
        heapq.heappush(small_max_heap, -num)
        if small_max_heap and large_min_heap and -small_max_heap[0]  > large_min_heap[0]:
            val = -heapq.heappop(small_max_heap)
            heapq.heappush(large_min_heap, val)

        if len(small_max_heap) > len(large_min_heap) + 1:
            val = -heapq.heappop(small_max_heap)
            heapq.heappush(large_min_heap, val)

        if len(large_min_heap) > len(small_max_heap) +  1:
            val = -heapq.heappop(large_min_heap)
            heapq.heappush(small_max_heap, val)


    def add_median():
        if len(small_max_heap) == len(large_min_heap):
            result.append((-small_max_heap[0] + large_min_heap[0]) // 2)
        elif len(small_max_heap) > len(large_min_heap):
            result.append((-small_max_heap[0]))
        else:
            result.append(large_min_heap[0])
    for num in stream:
        add_num(num)
        add_median()

    return result


lst1 =  [1, 2, 3, 4, 5]
lst1 =  [11, 2, 8, 23, 3, 2, 5]
lst1 = [5, 4, 10, 11, 1, 9, 8]
lst1 = [3, 1, 5, 2, 6]
lst1 =  [4, 3] #answer = 3
print(online_median_again(lst1))