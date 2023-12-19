class Solution:
    from typing import List
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        global time_stamp

        adj_list = [[] for _ in range(numCourses)]
        arr = [-1] * numCourses
        dep = [-1] * numCourses
        time_stamp = 0

        for course, pre_req in prerequisites:
            adj_list[pre_req].append(course)

        def has_cycle(node):
            global time_stamp
            time_stamp += 1
            arr[node] = time_stamp
            for nei in adj_list[node]:
                if arr[nei] == -1:
                    is_cycle = has_cycle(nei)
                    if is_cycle:
                        return True
                else:
                    # If arrival time is set, and departure time is not set, then there is a cycle
                    if dep[nei] == -1:
                        return True
            time_stamp += 1
            dep[node] = time_stamp
            return False

        for i in range(numCourses):
            if has_cycle(i):
                return False
        return True

sln = Solution()
print(sln.canFinish(2, [[1, 0]]) == True)