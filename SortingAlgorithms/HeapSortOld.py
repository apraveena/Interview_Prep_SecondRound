def has_left_child(idx, len):
    return 2 * idx <= len

def has_right_child(idx, len):
    return 2 * idx + 1 <= len

#Building max heap parsing from left to right
def build_max_heap(arr, n):
    for curr_idx in range(1, n):
        left_child_idx = 2 * curr_idx
        right_child_idx = left_child_idx + 1

        #left child
        if has_left_child(curr_idx,n-1) and arr[curr_idx] < arr[left_child_idx]:
            left_child = True
            arr[curr_idx], arr[left_child_idx] = arr[left_child_idx], arr[curr_idx]

        #right child
        if  has_right_child(curr_idx, n) and arr[right_child_idx] > arr[curr_idx]:
            right_child = True
            arr[curr_idx], arr[right_child_idx] = arr[right_child_idx], arr[curr_idx]

        if left_child or right_child:
            parent_idx = curr_idx // 2
            while parent_idx > 0 and arr[curr_idx] > arr[parent_idx]:
                arr[curr_idx], arr[parent_idx] = arr[parent_idx], arr[curr_idx]
    print(arr)


def extract_max(arr):
    max = arr[1]
    n = len(arr)
    for curr_idx in range(1, n):
        # parent_node_index = curr_idx // 2
        left_child_idx = 2 * curr_idx
        right_child_idx = left_child_idx + 1
        if has_left_child(curr_idx, n-1) and has_right_child(curr_idx, n-1):
            if arr[left_child_idx] > arr[right_child_idx]:
                arr[curr_idx], arr[left_child_idx] = arr[left_child_idx], arr[curr_idx]


    return max

def heap_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    arr.insert(0, -1)  # Sentinal value in the value
    build_max_heap(arr, len(arr)) #O(n)
    aux = []
    for i in range(len(arr)):
        aux.append(extract_max(arr))

    print(aux)
    return []

#From Udemy
def build_heap_top_down(a, n):
    for i in range(2, n+1):
	    restore_up(i, a)

def restore_up(i, a):
    k = a[i]
    iparent = i // 2
    while a[iparent] < k:
	    a[i] = a[iparent]
	    i = iparent
	    iparent = i // 2
    a[i] = k

#trying
def heap_sort(a):
    n = len(a)
    i = 1
    while n > 1:
        a[1], a[n-1] = a[n-1], a[1]
        n -= 1
        i += 1
        restore_up(i, a)

a2 = [99999, 20, 33, 15, 6, 40, 60, 45, 16, 75, 10, 80, 12]
n2 = len(a2)-1
print(a2)
build_heap_top_down(a2, n2)
for i in range(1, n2+1):
    print(a2[i], " ", end = '')
print()

# lst1 = [5, 8, 3, 9, 4, 1, 7]
# print(lst1)
# heap_sort(lst1)