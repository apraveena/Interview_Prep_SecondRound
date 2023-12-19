def minimum_cost(n_cities, connections):
    """
    Args:
     n_cities(int32)
     connections(list_list_int32)
    Returns:
     int32
    """
    # size = [1] * (n_cities + 1)
    # parent = [x for x in range(n_cities + 1)]
    # connections.sort(key=lambda item: item[2])
    # no_of_components = n_cities
    #
    # total_cost = 0
    #
    # def find(x):
    #     # base case
    #     if x == parent[x]:
    #         return x
    #
    #     root_x = find(parent[x])
    #     parent[x] = root_x
    #
    #     return root_x
    #
    # for u, v, cost in connections:
    #     root_u = find(u)
    #     root_v = find(v)
    #     if root_u != root_v:
    #         if size[root_u] < size[root_v]:
    #             parent[root_u] = root_v
    #             size[root_v] += size[root_u]
    #         else:
    #             parent[root_v] = root_u
    #             size[root_u] += size[root_v]
    #         no_of_components -= 1
    #         total_cost += cost
    #         if no_of_components == 1:
    #             break
    #
    # if no_of_components != 1:
    #     return -1
    # else:
    #     return total_cost

class Solution:
    from typing import List

    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        connections.sort(key=lambda x: x[2])
        components = n
        size = [1] * (n + 1)
        parent = [x for x in range(n + 1)]
        total_cost = 0
        result = []

        # find using path compression
        def find_parent(x):
            # Base case
            if x == parent[x]:
                return x
            # recursive case find the rootx of parent bottom up
            rootx = find_parent(parent[x])
            # now set the parent[x] directly to the top rootx
            parent[x] = rootx
            return rootx
        # union will take o(n)
        for u, v, cost in connections:
            lu = find_parent(u)
            lv = find_parent(v)
            if lu != lv:
                if size[lu] < size[lv]:
                    parent[lu] = lv
                    size[lv] += size[lu]
                else:
                    parent[lv] = lu
                    size[lu] += size[lv]
                components = components - 1
                total_cost += cost
                result.append((u, v))

        if components != 1:
            return -1
        else:
            return total_cost

sln = Solution()
print(sln.minimumCost(7,  [[1,2,1],[1,3,2],[2,3,3], [4,5,4],[5,6,5], [6,3,6], [7, 6, 7]]) == 6)
print(sln.minimumCost(3,  [[1,2,5],[1,3,6],[2,3,1]]) == 6)
# print(sln.minimumCost(4,  [[1, 3, 1],[2, 4, 1]]) == -1)