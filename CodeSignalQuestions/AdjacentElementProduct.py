'''
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
solution(inputArray) = 21.

7 and 3 produce the largest product.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer inputArray

An array of integers containing at least two elements.

Guaranteed constraints:
2 ≤ inputArray.length ≤ 10,
-1000 ≤ inputArray[i] ≤ 1000.

[output] integer

The largest product of adjacent elements.
'''
def largest_product_adjacent(inputArray):
    max_product = inputArray[0] * inputArray[1]
    for i in range(1, len(inputArray) - 1):
        curr_product = inputArray[i] * inputArray[i + 1]
        max_product = max(curr_product, max_product)
    return max_product

def largest_product_adjacent_sliding_window(inputArray):
    curr_product = max_product = inputArray[0] * inputArray[1]
    for i in range(1, len(inputArray) - 1):
        curr_product = curr_product/inputArray[i]*inputArray[i+1]
        max_product = max(max_product, curr_product)
    return max_product

def test_adjacent_element_product():
    print()
    list1 = [3, 6, -2, -5, 7, 3]
    print(largest_product_adjacent(list1) == 21)
    print(largest_product_adjacent_sliding_window(list1) == 21)
