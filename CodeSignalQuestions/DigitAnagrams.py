
def solution(a):
    freq = {}
    for num in a:
        str_num = "".join(sorted(str(num)))
        freq[str_num] = freq.get(str_num, 0) + 1
    print(freq)
    count = 0
    for value in freq.values():
        count += value * (value - 1) // 2

    return count
print(solution([25, 35, 872, 228, 53, 278, 872]))

print(solution([25, 35, 872, 222, 54, 278, 372]))


# def solution(a):
#     global count
#     num_a = [str(num) for num in a]
#     count = 0
#
#     def are_anagrams(str1, str2):
#         if sorted(str1) == sorted(str2):
#             return True
#
#     def helper(num, arr):
#         global count
#         for item in arr:
#             if are_anagrams(item, num):
#                 count += 1
#
#     for i, num in enumerate(num_a):
#         helper(num, num_a[i + 1:])
#
#     return count




