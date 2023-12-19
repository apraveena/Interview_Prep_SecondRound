from typing import List

def get_kth_largest_element(arr: List[int], k:int) -> int:
    k = len(arr)-k #2nd largest element would be length-2 index if we sort the list
    #In quick_select, we dont need to sort the whole array, only sort the side the value exists
    def quick_select(l, r):
        pivot, p = arr[r], l
        for i in range(l, r):
            if arr[i] <= pivot:
                arr[i], arr[p] = arr[p], arr[i]
                p += 1
        arr[p], arr[r] = arr[r], arr[p]

        if p > k: return quick_select(l, p - 1)
        elif p < k: return quick_select(p + 1, r)
        else: return arr[p]

    return quick_select(0, len(arr)-1)

lst1 = [4, 6, 7, 3, 6, 7, 1, 2, 3]
print(get_kth_largest_element(lst1, 3))
