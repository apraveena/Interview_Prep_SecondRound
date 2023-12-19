def course_schedule(n, prerequisites):
    """
    Args:
     n(int32)
     prerequisites(list_list_int32)
    Returns:
     list_int32
    """
    adj_list = [[] for _ in range(n)]
    arr = [-1] * n
    dep = [-1] * n
    results = []
    time_stamp = [0]

    if not n:
        return [-1]

    for course, pre_req in prerequisites:
        adj_list[pre_req].append(course)

    def has_cycle(node):
        time_stamp[0] += 1
        arr[node] = time_stamp[0]
        for nei in adj_list[node]:
            if arr[nei] == -1:
                is_cycle = has_cycle(nei)
                if is_cycle:
                    return True
            elif dep[nei] == -1:
                return True

        time_stamp[0] += 1
        dep[node] = time_stamp[0]
        results.append(node)
        return False

    for i in range(n):
        if arr[i] == -1:
            if has_cycle(i):
                return [-1]

    if len(results) < n:
        return [-1]
    results.reverse()
    return results

from collections import deque
def course_shedule_usingBFS(n, prerequisites):
    if n == 0:
        return -1
    # Build the graph
    adj_list = [[]for _ in range(n)]
    in_degree = [0] * (n)
    for course, prerequisite in prerequisites:
        adj_list[prerequisite].append(course)
        in_degree[course] += 1
    q = deque()
    order = []
    # outer loop first
    for i in range(n):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        curr = q.popleft()
        order.append(curr)
        for nei in adj_list[curr]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                q.append(nei)

    if len(order) < n:
        return [-1]
    return order

#[[1, 0], [2, 0], [3, 1], [3, 2]]
#1 is dependent on 0 so 0 is a pre-req of 1. 2 is dependent on 0 so 0 is also a prereq of 2 ...
# in_degree should be [0, 1, 1, 2] --> 0 is not dependent on anyone, 1 is dependent on 0, so degree is 1
#   2 is dependent on 0, so in-degree 1, 3 is dependent on both 1 and 2, so, degree is 2
#0 --> 1 --> 3 and 0 --> 2 --> 3 = complete path = 0 --> 1 --> 2 --> 3 or 0 --> 2 --> 1 --> 3
#Adjacency list is [[1, 2], [3], [3], []]
def course_schedule_bfs_mytry(n, prerequisites):
    adj_list = [[] for _ in range(n)]
    in_degree = [0] * n

    for course, prereq in prerequisites:
        adj_list[prereq].append(course)
        in_degree[course] += 1

    path = []
    q = deque()
    for idx, in_deg in enumerate(in_degree):
        if in_deg == 0:
            q.append(idx)

    while q:
        curr = q.popleft()
        path.append(curr)
        for nei in adj_list[curr]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                q.append(nei)

    return path



prerequisites=[
[1, 0],
[2, 0],
[3, 1],
[3, 2]
]
print(course_schedule_bfs_mytry(4,prerequisites))


# print(course_schedule(4, [[1, 0],[2, 0],[3, 1],[3, 2]]) in ([0, 2, 1, 3], [0, 1, 2, 3]))