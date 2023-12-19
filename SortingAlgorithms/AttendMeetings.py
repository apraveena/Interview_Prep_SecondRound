def can_attend_all_meetings_brute_force(intervals):
    """
    Args:
     intervals(list_list_int32)
    Returns:
     int32
    """
    #Brute force - failing some cases
    for i in range(len(intervals)):
        curr = intervals[i]
        for j in range(i + 1, len(intervals)):
            next = intervals[j]
            if curr[1] > next[0] and curr[0] < next[1]:
                return 0
    return 1

#Optimal

def can_attend_all_meetings(intervals):
    """
    Args:
     intervals(list_list_int32)
    Returns:
     int32
    """
    intervals = sorted(intervals, key=lambda x: x[0])
    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i + 1][0]:
            return 0
    return 1


intervals = [[1, 5], [5, 8], [10, 15]]
intervals = [[13, 56],[1, 3],[4, 5],[9990, 10341],[8, 10],[67, 9990]]
intervals = [[13, 56],[1, 6],[4, 5],[9990, 10341],[8, 10],[67, 9990]]
print(can_attend_all_meetings(intervals))