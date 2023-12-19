def convert_edge_list_to_adjacency_list(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     list_list_int32
    """
    adj_list = [[] for _ in range(n)]
    for from_edge, to_edge in edges:
        adj_list[from_edge].append(to_edge)
        adj_list[to_edge].append(from_edge)

    return adj_list

n = 5
edges = [[0, 1],[1, 4],[1, 2],[1, 3],[3, 4]]
print(convert_edge_list_to_adjacency_list(n, edges))