from typing import List, Dict
import random

#Both of the following quesitons have same pattern
#692. Top k frequent words
#347. Top k frequent elements


#using in-built sorted function - not sure if that is correct
# dont understand -kv -- update (just negating the number so the order can be reversed later)
#Turns out this is brute force approach.
#Solution not correct
#brute_force?
def find_top_k_frequent_elements_with_heap(arr, k):
    """
    Args:
     arr(list_int32)
     k(int32)
    Returns:
     list_int32
    """
    hmap = {}
    #store the frequency of each element
    for item in arr:
        hmap[item] = hmap.get(item, 0) + 1

    #can we use heapq.heapify(hmap.items) instead of sorted - both have nlogn complexity.
    # Just foundout that heapify is unstable sort whereas sorted is.
    # It doesn't matter for numbers, but for objects or tuples.
    res = sorted(hmap.items(), key=lambda kv: (-kv[1], kv[0]))
    #we do -ve frequency so the sort can be reversed by frequency.


    # res1 = []
    # for i, item in enumerate(res):
    #     res1.append(item[0])
    #     if i+1 == k:
    #         break
    # return res1
    #shorterning hte above code
    return [item[0] for idx, item in enumerate(res) if idx < k ]

#Quick select approach
#Not working consistently
#----------------From here-----------------------
def partition(unique, low, high, frequency):
    random_pivot_index = random.randint(low + 1, high)
    print(f"low: {low + 1}, high: {high} and random: {random_pivot_index}")
    pivot_freq = frequency[random_pivot_index]
    unique[random_pivot_index], unique[high] = unique[high], unique[random_pivot_index]
    i = low
    for j in range(low, high):
        if frequency[unique[j]] <= pivot_freq:
            unique[i], unique[j] = unique[j], unique[i]
            i += 1
        unique[i], unique[high] = unique[high], unique[i]
    return i

def quick_select(unique: List[int], k: int, frequency: Dict[int, int]):
	low, high = 0, len(unique) - 1
	while low <= high:
		pivot = partition(unique, low, high, frequency)
		if pivot == len(unique)-k:
			return
		elif pivot > len(unique) - k:
			high = pivot - 1
		else:
			low = pivot + 1

def find_top_k_frequent_elements_quick_select(arr, k):
	frequency = {}
	for i in range(len(arr) - 1):
		frequency[arr[i]] = frequency.get(arr[i], 0) + 1

	unique = []
	for it in frequency:
		unique.append(it)

	quick_select(unique, k, frequency)
	res = []
	for i in range(len(unique)-k, len(unique)):
		res.append(unique[i])
	return res
#--------------------quick select - to here--------------------------------
#-----------------Counting sort code starts here---------------------------
#O(n) - from ik code.. not working
def find_top_k_frequent_elements_counting_sort(arr, k):
	frequency = {}
	numbers = []
	taken = {}

	for i in range(len(arr)):
		frequency[arr[i]] = frequency.get(arr[i],0) + 1
	for i in range(len(arr)):
		if taken[arr[i]]:
			continue
		else:
			taken[arr[i]] = True
			numbers[frequency[arr[i]]].append(arr[i])
	for i in range(len(arr)):
		while len(numbers[i]) > 0 and k > 0:
			k -= 1
			result.append(numbers[i][-1]) # I think
			result.pop()

		if k==0:
			break
	return result
#------------------Counting sort code ends here---------------------------

lst1 =  [1, 2, 3, 2, 4, 3, 1, 3]
print(find_top_k_frequent_elements_with_heap(lst1, 2))
print(find_top_k_frequent_elements_quick_select(lst1, 2))
print(find_top_k_frequent_elements_counting_sort(lst1, 2))