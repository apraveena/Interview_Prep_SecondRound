#counting sort is about storing frequencies of elements in a collection
#There are 2 styles in this file (counting_sort_again and counting_sort_ik) that both work
#the first one (counting_sort).. not sure if it is correct as we are using dictionary (as it is not ordered)

#Time complexity of counting sort is O(n)

#This will work for ordered dictionary
#But if it's not, the order matters for this problem.. does it work always?
#also, this is using another auxiliary space for result
def counting_sort(a):
    d, result = {}, []
    for item in a:
        if item < -400000 or item > 400000:
            return a
        d[item] = d.get(item, 0) + 1

    for k, v in d.items():
        for _ in range(v):
            result.append(k)
    return result

#I wrote this and this works!!
#From neetcode?
def counting_sort_again(a):
    low = min(a)
    high = max(a)
    # to accommodate negative numbers, create a list with the size as whole range of numbers
    count_list = [0] * (high - low + 1)
    result = []

    #Populate count list with the frequencies as the value and the range of numbers as indices
    #for eg: if original list is [-4, 1, 0, 1, 3]
    #count_list = [0, 0, 0, 0, 0, 0, 0, 0]
    #representing frequences of [-4, -3, -2, -1, 0, 1, 2, 3]
    # it will be updated with data as
    #count_list = [1, 0, 0, 0, 1, 2, 0, 1]
    for i, val in enumerate(a):
        count_list[val - low] += 1

    #In result list, add the numbers from left to right as their frequencies
    #in the example above -4 occurs 1 from count_list and 1 occurs twice
    for i, val in enumerate(count_list):
        val_to_append = i + low #to accommodate negative values
        for j in range(val):
            result.append(val_to_append)

    return result

#someone else's code - works
def counting_sort1(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    m = min(arr)
    k = max(arr) - m
    bucket = [0] * (k+1)
    for i in arr:
        bucket[i-m] += 1
    arr=[]
    num = m
    for i in bucket:
        while i>0:
            arr.append(num)
            i-=1
        num+=1
    return arr

#This make sense.. no auxiliary array.
#Final
def counting_sort_ik(arr):
    frequencies = {}
    for item in arr:
        frequencies[item] = frequencies.get(item, 0) + 1
        # if item in frequencies:
        #     frequencies[item] += 1
        # else:
        #     frequencies[item] = 1
        #item is key, frequency is value

    low, high = min(arr), max(arr)
    arr_index = 0
    for i in range(low, high + 1):
        curr_frequency = frequencies.get(i, 0) #mychange from ik
        while curr_frequency > 0:
            arr[arr_index] = i
            arr_index += 1
            curr_frequency -= 1
    return arr

#This uses the cumulative sum list from online
def counting_sort_from_Suneetha(inputArray):
    if len(inputArray) == 1:
        return inputArray

    # Creates 2D list of size max number in the array
    max_element = max(inputArray)
    min_element = min(inputArray)
    countArrayLength = (max_element - min_element) + 1
    counts = [0] * countArrayLength
    print(counts)

    # Finds the "counts" for each individual number
    for i in range(len(inputArray)):
        counts[inputArray[i] - min_element] += 1
    print(counts)

    # Finds the cumulative sum counts
    for index in range(1, len(counts)):
        counts[index] = counts[index - 1] + counts[index]
    print(counts)

    # Sorting Phase
    outputArr = [0] * len(inputArray)
    i = len(inputArray) - 1

    while i >= 0:
        currentElement = inputArray[i]
        counts[currentElement] -= 1
        newposition = counts[currentElement-min_element]
        outputArr[newposition] = currentElement
        i = i - 1
    return outputArr

lst1 = [5, 8, 3, 9, 4, 1, 7]
lst1 = [15, -16, 10, 11, 1, -6, 7, 8, 3, 9, 4, 1, 7]
lst1 = [-2, 6, 3, 1, 3]
# lst1 = [7, 7, 7, 7, 7]
# lst1 =  [5, 8, 3, 9, 4, 1, 7]
lst1 = [-4, 1, 6, 8,6, 2, 2, 3,4, 7,1,1,1,1]
print(lst1)
print(counting_sort_ik(lst1))


