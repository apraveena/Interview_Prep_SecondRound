#Eulerian path exists when eulierian cycle exists (all degrees are even) or
# when the number of odd degrees is exactly 2
# degree = number of edges from a node (or vertex)
def check_if_eulerian_path_exists(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     bool
    """
    degrees = {}
    for edge in edges:
        from_edge = edge[0]
        to_edge = edge[1]
        degrees[from_edge] = degrees.get(from_edge, 0) + 1
        degrees[to_edge] = degrees.get(to_edge, 0) + 1

    odd_count = 0
    for val in degrees.values():
        if val % 2 == 1:
            odd_count += 1

    return odd_count in (2, 0)