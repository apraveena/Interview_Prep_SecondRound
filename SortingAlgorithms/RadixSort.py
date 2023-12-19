#get the digit in the given place
def get_place_digit(num, place):
    d = 0
    for i in range (1, place+1):
        d = num % 10
        num //= 10
    return d

#calculate number of digits in the largest number
#not using it
def digits_in_largest(num):
    counter = 1
    num //= 10
    while num > 0:
        num //= 10
        counter += 1
    return counter

def counting_sort(arr, place):
    size = len(arr)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements.
    for i in range(0, size):
        index = arr[i] // place
        count[index % 10] += 1

    # Calculate cumulative count.
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order.
    i = size - 1
    while i >= 0:
        index = arr[i] // place
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        arr[i] = output[i]


def radix_sort(arr):
    # Get maximum element
    max_element = max(arr)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        counting_sort(arr, place)
        place *= 10

    return arr

# print(digits_in_largest(4))
# print(get_place_digit(248, 2))
lst = [345, 253, 676, 88, 43, 10, 4, 354, 786, 4, 77, 87]
print(lst)
print(radix_sort(lst))
#expected output = [4, 4, 10, 43, 77, 87, 88, 253, 345, 354, 676, 786 ]

# lst = [-3, 4, 1, 4, 3, 2, 2, 1, 3, 5, -4]
# print(counting_sort(lst))
