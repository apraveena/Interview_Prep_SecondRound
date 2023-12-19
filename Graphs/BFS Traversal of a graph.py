def bfs_traversal(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     list_int32
    """
    q = deque()
    graph = [[] for _ in range(n)]
    visited = [0] * n
    result = []

    def build_adj_list(n, edges):
        for from_edge, to_edge in edges:
            graph[from_edge].append(to_edge)
            graph[to_edge].append(from_edge)

    build_adj_list(n, edges)

    def bfs_helper(node):
        if not visited[node]:
            visited[node] = True
            result.append(node)
            q.append(node)

        while q:
            curr = q.popleft()
            for nei in graph[curr]:
                if not visited[nei]:
                    q.append(nei)
                    result.append(nei)
                    visited[nei] = True

    for i in range(n):
        if not visited[i]:
            bfs_helper(i)

    return result

