def convert_edge_list_to_adjacency_matrix(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     list_list_bool
    """
    result = [[False for i in range(n)] for _ in range(n)]
    for from_edge, to_edge in edges:
        result[from_edge][to_edge] = True
        result[to_edge][from_edge] = True

    return result
