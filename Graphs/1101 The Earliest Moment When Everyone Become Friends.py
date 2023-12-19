class Solution:
    from typing import List
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        parent = [x for x in range(n)]
        size = [1] * n
        no_of_components = n

        def find_parent(x):
            while parent[x] != x:
                x = parent[x]

            return x

        for t, u, v in logs:
            parent_u = find_parent(u)
            parent_v = find_parent(v)
            if parent_u != parent_v:
                if size[parent_u] < size[parent_v]:
                    parent[parent_u] = parent_v
                    size[parent_v] += size[parent_u]
                else:
                    parent[parent_v] = parent_u
                    size[parent_u] += size[parent_v]
                no_of_components -= 1
                if no_of_components == 1:
                    return t

        return -1

sln = Solution()
print(sln.earliestAcq([[9,3,0],[0,2,1],[8,0,1],[1,3,2],[2,2,0],[3,3,1]], 4))