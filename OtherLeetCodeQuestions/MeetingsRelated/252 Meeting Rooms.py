'''
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Input: intervals = [[7,10],[2,4]]
Output: true
'''

from typing import List

#Time complexity -> O(nlogn) + O(n) = O (nlogn)
#Sort = O(nlogn)
#Iterating = O(n)
def can_attend(intervals: List[List[int]]) -> bool:
    intervals.sort()
    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i + 1][0]:
            return False
    return True