# You
# are
# given
# an
# array
# of
# integers
# nums, there is a
# sliding
# window
# of
# size
# k
# which is moving
# from the very
#
# left
# of
# the
# array
# to
# the
# very
# right.You
# can
# only
# see
# the
# k
# numbers in the
# window.Each
# time
# the
# sliding
# window
# moves
# right
# by
# one
# position.
#
# Return
# the
# max
# sliding
# window.
#
# Example
# 1:
#
# Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
# Output: [3, 3, 5, 5, 6, 7]
# Explanation:
# Window
# position
# Max
# ---------------               -----
# [1  3 - 1] - 3
# 5
# 3
# 6
# 7
# 3
# 1[3 - 1 - 3]
# 5
# 3
# 6
# 7
# 3
# 1
# 3[-1 - 3
# 5] 3
# 6
# 7
# 5
# 1
# 3 - 1[-3
# 5
# 3] 6
# 7
# 5
# 1
# 3 - 1 - 3[5
# 3
# 6] 7
# 6
# 1
# 3 - 1 - 3
# 5[3
# 6
# 7]      7
# Example
# 2:
#
# Input: nums = [1], k = 1
# Output: [1]


#Brute force
def sliding_window_max(list1, k):
    new_list = []
    new_list.append(max(list1[:k]))
    for i in range(1, len(list1) - k + 1):
        new_list.append(max(list1[i: i + k]))

    return new_list

# print(sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3))
# print(sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7])

import collections
def sliding_window_max_without_max(list1, k):
    d = collections.deque()
    def push_in(val):
        while d and d[-1] < val:
            d.pop()
        d.append(val)

    for i in range(k):
        push_in(list1[i])

    result = [d[0]]

    for i in range(k, len(list1)):
        if d[0] == list1[i - k]:
            d.popleft()
        push_in(list1[i])
        result.append(d[0])

    return result

print(sliding_window_max_without_max([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7])
