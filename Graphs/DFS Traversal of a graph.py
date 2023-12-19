def dfs_traversal(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     list_int32
    """
    visited = [0] * n
    graph = [[] for _ in range(n)]
    result = []
    for from_edge, to_edge in edges:
        graph[from_edge].append(to_edge)
        graph[to_edge].append(from_edge)

    def dfs(s):
        visited[s] = 1
        result.append(s)
        for nei in graph[s]:
            if not visited[nei]:
                visited[nei] = 1
                dfs(nei)

    for i in range(n):
        if not visited[i]:
            dfs(i)

    return result

