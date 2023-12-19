def pair_sum_sorted_array(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    left = 0
    right = len(numbers) - 1
    while left < right:
        curr_sum = numbers[left] + numbers[right]
        if curr_sum > target:
            right -= 1
        elif curr_sum < target:
            left += 1
        else:
            return [left, right]
    return [-1, -1]

numbers =  [1, 2]
target = 4