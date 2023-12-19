class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(n + 1)]
        visited = [-1] * (n + 1)
        color = [-1] * (n + 1)
        colors = ["red", "blue"]
        adj_list = [[] for _ in range(n + 1)]
        for [from_edge, to_edge] in dislikes:
            adj_list[from_edge].append(to_edge)
            adj_list[to_edge].append(from_edge)

        def can_bipartite(node, curr_color):
            color[node] = colors[curr_color]
            visited[node] = 1
            nei_color = not curr_color
            for nei in adj_list[node]:
                if visited[nei] == -1:
                    visited[nei] = 1
                    is_bipartite = can_bipartite(nei, nei_color)
                    if not is_bipartite:
                        return False
                else:
                    if color[node] == color[nei]:
                        return False
            return True

        for i in range(n):
            if visited[i] == -1:
                res = can_bipartite(i, 0)
                if not res:
                    return False
        return True
