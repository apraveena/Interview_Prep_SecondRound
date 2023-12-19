from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        visited = [0] * n
        no_of_components = 0

        def build_adj_list():
            for from_edge, to_edge in edges:
                adj_list[from_edge].append(to_edge)
                adj_list[to_edge].append(from_edge)

        def dfs(s):
            visited[s] = 1
            for nei in adj_list[s]:
                if not visited[nei]:
                    visited[nei] = 1
                    dfs(nei)

        build_adj_list()
        for i in range(n):
            if not visited[i]:
                no_of_components += 1
                dfs(i)

        return no_of_components

def number_of_connected_components(n, edges):
    from collections import deque
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     int32
    """
    if not n or not edges:
        return 0

    adj_list = [[] for _ in n]
    for from_edge, to_edge in edges:
        adj_list[from_edge].append(to_edge)
        adj_list[to_edge].append(from_edge)

    visited = [-1] * n

    def bfs(node):
        q = deque()
        q.append(node)
        visited[node] = 1
        while q:
            curr = q.pop()
            for nei in adj_list[curr]:
                if visited[nei] == -1:
                    visited[nei] = 1
                    q.append(nei)

    no_of_connected_components = 0
    for i in range(n):
        if visited[i] == -1:
            no_of_connected_components += 1
            bfs(i)

    return no_of_connected_components


# sln = Solution()
# print(sln.countComponents(5, [[0,1],[1,2],[3,4]]) == 2)
print(number_of_connected_components(5, [[0,1],[1,2],[3,4]]) == 2)