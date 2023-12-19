def no_of_subarrays_with_threshold_greater_or_equals(input_list, k, threshold):
    count = 0
    curr_sum = sum(input_list[:k])
    if curr_sum >= threshold * k:
        count += 1

    for i in range(k, len(input_list)):
        curr_sum += input_list[i] - input_list[i - k]
        if curr_sum >= threshold * k:
            count += 1

    return count

print(no_of_subarrays_with_threshold_greater_or_equals([2, 2, 2, 2, 5, 5, 5, 8], 3, 4) == 3)
print(no_of_subarrays_with_threshold_greater_or_equals([1, 1, 1, 1, 1], 1, 0) == 5)
print(no_of_subarrays_with_threshold_greater_or_equals([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5) == 6)
print(no_of_subarrays_with_threshold_greater_or_equals([7, 7, 7, 7, 7, 7, 7], 7, 7) == 1)
print(no_of_subarrays_with_threshold_greater_or_equals([4, 4, 4, 4], 4, 1) == 1)
