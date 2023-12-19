class Solution:
    from typing import List

    def isBipartite(self, graph: List[List[int]]) -> bool:
        from collections import deque
        n = len(graph)
        visited = [-1] * n
        level = [-1] * n
        parent = [-1] * n

        def bfs(node):
            q = deque()
            q.append(node)
            while q:
                curr = q.popleft()
                visited[curr] = 1
                for nei in graph[curr]:
                    if visited[nei] == -1:
                        visited[nei] = 1
                        parent[nei] = curr
                        level[nei] = level[curr] + 1
                        q.append(nei)
                    else:
                        #if cycle and cross edge between same level nodes, no bipartite
                        if parent[curr] != nei and level[nei] == level[curr]:
                            return False

            return True

        for i  in range(n):
            level[i] = i
            if visited[i] == -1:
                is_bipartite = bfs(i)
                if not is_bipartite:
                    return False

        return True

sln = Solution()
# print(sln.isBipartite([[1,3],[0,2],[1,3],[0,2]]) == True)
# print(sln.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]) == False)
print(sln.isBipartite([[4,1],[0,2],[1,3],[2,4],[3,0]]) == False) #test why popleft worked and not pop() #with pop,code acted like dfs only picking the last element and then child of last element etc..
# print(sln.isBipartite([[4],[],[4],[4],[0,2,3]]) == True)