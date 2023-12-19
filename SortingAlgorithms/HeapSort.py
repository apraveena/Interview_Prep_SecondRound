def restore_up(a, i):
    parent_idx = i//2
    while a[parent_idx] < a[i]:
        a[parent_idx], a[i] = a[i], a[parent_idx]
        i = parent_idx
        parent_idx //= 2

#0th element is Sentinal value
# From beginning, come down one step and restore up with parent
def build_max_heap(a, n):
    for i in range(2, n):
        restore_up(a, i)

def heapify(arr, i, n):
    left = 2 * i
    right = 2 * i + 1
    if left <= n and right <= n: #If both and left nodes exist
        max_idx = left if arr[left] >= arr[right] else right
    elif left <= n: #only left node exist
        max_idx = left
    else:
        return
    #Swap if root value is less than children's value
    if arr[i] < arr[max_idx]:
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
        heapify(arr, max_idx, n)

#Build - Extract - Heapify
#build heap (in this case max heap) first (also called heapify in some places)
#Move the first item which is max to the end. heapify first item so it finds its place O(log n)
#consider the size of array as one lesser so we are not looking at the last element
#repeat again - this time, move the first item to end - 1 and size becomes n-2
def heap_sort(a):
    n = len(a)
    build_max_heap(a, n)
    while n > 1:
        a[n-1], a[1] = a[1], a[n-1]
        n -= 1
        heapify(a, 1, n-1)


a2 = [99999, 20, 33, 15, 6, 40, 60, 45, 16, 75, 10, 80, 12]
# a2 = [99999, 20, 33, 15, 6, 40]
print(a2)
# build_heap(a2, len(a2))
heap_sort(a2)
print(a2)

#----------------build_min_heap code here--------------
def is_leaf(n, i):
    return i * 2 >= n

def restore_down(arr, i, n):
    left_child = 2 * i
    right_child = 2 * i + 1

    has_left_child = n >= left_child
    has_right_child = n >= right_child

    if not (has_right_child or has_left_child):
        return

    if has_left_child and has_right_child:
        if arr[left_child] < arr[right_child]:
            min_idx = left_child
        else:
            min_idx = right_child
    elif has_left_child:
        min_idx = left_child
    else:
        min_idx = right_child

    if arr[i] > arr[min_idx]:
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        restore_down(arr, min_idx, n)

def build_min_heap(arr):
    n = len(arr)
    arr.insert(0, 99999)
    for i in range(n, 0, -1 ):
        if is_leaf(n+1, i):
            continue
        restore_down(arr, i, n)
    return arr
