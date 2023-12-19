from typing import List


def is_number(input_str):
  # Convert input to a string if it's not already
  input_str = str(input_str)

  # Check if the string starts with a minus sign (for negative numbers)
  if input_str.startswith('-'):
    return input_str[1:].isdigit()  # Check if the rest are digits

  # Check if the string is composed of digits (for positive numbers)
  return input_str.isdigit()



def sequences(nums: List[int]):
  res = []
  if not nums:
    return [[]]
  if len(nums) == 1:
    return [nums]
  ptr1, ptr2 = 0, 1
  while ptr1 < len(nums) - 2 and ptr2 < len(nums) - 1:
    temp = []
    temp.append(nums[ptr1])
    while is_number(str(nums[ptr1])) and is_number(str(nums[ptr2])) and nums[ptr2] == nums[ptr1] + 1:
      temp.append(nums[ptr2])
      ptr1 += 1
      ptr2 += 1
      if ptr1 > len(nums) - 2 or ptr2 > len(nums) - 1:
        break
    if len(temp) > 1:
      res.append(temp[:])
    ptr1 += 1
    ptr2 += 1
  return res

print(sequences([1, 2, 3, 5, 9, 'a', 6, 7, 8, 4, '@', -5, -7, -3, -2, -1]) == [[1, 2, 3], [6, 7, 8], [-3, -2, -1]])