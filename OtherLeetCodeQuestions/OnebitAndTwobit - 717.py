'''
717. 1-bit and 2-bit Characters
https://leetcode.com/problems/1-bit-and-2-bit-characters/
We have two special characters:

The first character can be represented by one bit 0.
The second character can be represented by two bits (10 or 11).
Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.



Example 1:

Input: bits = [1,0,0]
Output: true
Explanation: The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.
Example 2:

Input: bits = [1,1,1,0]
Output: false
Explanation: The only way to decode it is two-bit character and two-bit character.
So the last character is not one-bit character.
'''

def is_one_bit_iterative(bits):
    i = 0
    while i < len(bits):
        next = i + 1
        if next < len(bits): #if there is next element
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        else:
            return bits[i] == 0
    return False

def is_one_bit_recursive(bits):
    if bits == [0] or bits == [0, 0]:
        return True
    elif bits == [1, 0] or bits == [1, 1] or bits == [0, 1]:
        return False
    else:
        if bits[0] == 0:
            return is_one_bit_recursive(bits[1:])
        else:
            return is_one_bit_recursive(bits[2:])

def is_one_bit_recursive1(bits):
    if bits == [0]:
        return True
    if bits == [1, 0]:
        return False
    if bits == [1]:
        return False

    if bits[0] == 0:
        return is_one_bit_recursive1(bits[1:])
    else:
        return is_one_bit_recursive1(bits[2:])

# lst = [1, 0, 0]
# # print(lst)
# print(is_one_bit_recursive1(lst)) #True
lst = [1, 1, 1, 0]
# # print(lst)
# print(is_one_bit_recursive1(lst)) #False
lst = [1, 1, 0, 0]
# # print(lst)
# print(is_one_bit_recursive1(lst)) #True
lst = [1, 1, 0, 1]
# print(lst)
print(is_one_bit_recursive1(lst)) #False





















