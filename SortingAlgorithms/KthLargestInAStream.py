import heapq
'''
From ik class problems
using min heap solution
    heap size from initial stream is of length k
    iterate over the rest of the elements from initial stream and only keep max k numbers in the heap
    Repeat the same with append stream. iterate over append stream
      and only keep max k numbers by popping the top element if it is smaller than element from append stream

The heappushpop function first pushes the provided element to the heap 
and then pops the smallest element from the heap, 
and the heapreplace function first pops the smallest element from the heap 
and then pushes the provided element back into the heap.
'''
def kth_largest_with_heapify(k, initial_stream, append_stream):
    arr = initial_stream[:k]
    heapq.heapify(arr)
    result = []
    for i in range(k, len(initial_stream)):
        if arr[0] < initial_stream[i]:
            heapq.heapreplace(arr, initial_stream[i]) #first pop the smallest element and push the provided element

    for item in append_stream:
        if len(arr) < k:
            heapq.heappush(arr, item)
        elif arr[0] < item:
            heapq.heappushpop(arr, item) #first pushes the element and then pops the smallest element
        result.append(arr[0])
    return result


i_stream = [4, 6]
a_stream = [5, 2, 20]
k = 2
i_stream = [5, 6, 2, 8, 1, 3]
a_stream = [16, 5, 12, 20]
k = 3
i_stream = [1000_000_000]
a_stream =  [100_000_000]
k = 2
print(i_stream)
print(a_stream)
print(k)
print(kth_largest_with_heapify(k, i_stream, a_stream))