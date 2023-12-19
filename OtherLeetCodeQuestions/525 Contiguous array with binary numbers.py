def longest_contiguous_arr(nums):
    hmap, count, max_len = {}, 0, 0
    hmap[0] = -1
    for i in range(len(nums)):
        if nums[i] == 0:
            count -= 1
        else:
            count += 1

        if count in hmap:
            max_len = max(max_len, i - hmap[count])
        else:
            hmap[count] = i
    return max_len

print(longest_contiguous_arr([0, 1]) == 2)
print(longest_contiguous_arr([0, 1, 0, 1]) == 4)
print(longest_contiguous_arr([0, 1, 0, 1, 0]) == 4)
print(longest_contiguous_arr([0, 1, 0, 0, 1, 0]) == 4) # 1001

