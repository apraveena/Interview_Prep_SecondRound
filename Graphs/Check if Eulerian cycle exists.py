#Eulerian cycle exists in a graph when the degree of any vertex is odd
def check_if_eulerian_cycle_exists(n, edges):
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

    for value in degrees.values():
        if value % 2 == 1:
            return False
    return True

print(check_if_eulerian_cycle_exists(5,[[0, 1], [1, 2], [1, 4], [2, 4]] ))