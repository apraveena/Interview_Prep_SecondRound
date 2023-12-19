#Used union find because of less time complexity
class Solution:
    from typing import List
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        # adj_list = [[] for _ in range(n + 1)]

        parent = [x for x in range(n + 1)]
        size = [1 for _ in range(n + 1)]
        no_of_components = n

        def find_parent(x):
            if parent[x] == x:
                return x
            parent[x] = find_parent(parent[x])
            return parent[x]

        for i in range(1 , n + 1):
            for j in range(1, n + 1):
                if i != j and isConnected[i-1][j-1] == 1:
                    i_parent = find_parent(i)
                    j_parent = find_parent(j)
                    if i_parent != j_parent:
                        if size[i_parent] > size[j_parent]:
                            parent[j_parent] = i_parent
                            size[i_parent] += size[j_parent]
                        else:
                            parent[i_parent] = j_parent
                            size[j_parent] += size[i_parent]
                        no_of_components -= 1

        return no_of_components

sln = Solution()
print(sln.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]) == 2)
print(sln.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]) == 3)