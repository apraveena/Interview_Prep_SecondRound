#DFS style
def is_it_a_tree(n, edge_start, edge_end):
    """
    Args:
     node_count(int32)
     edge_start(list_int32)
     edge_end(list_int32)
    Returns:
     bool
    """
    parent = [-1] * n
    visited = [0] * n
    adj_list = [[] for _ in range(n)]

    for i in range(len(edge_start)):
        adj_list[edge_start[i]].append(edge_end[i])
        adj_list[edge_end[i]].append(edge_start[i])

    def has_cycle(s):
        visited[s] = 1
        for nei in adj_list[s]:
            if not visited[nei]:
                visited[s] = 1
                parent[nei] = s
                if has_cycle(nei):
                    return True
            else:
                if parent[s] != nei:
                    return True
        return False
    components = 0
    for i in range(n):
        if not visited[i]:
            components += 1
            if components > 1: return False
            is_cycle = has_cycle(i)
            if is_cycle:
                return False
    return True


import collections

def is_it_a_tree_Sunee(node_count, edge_start, edge_end):
    # Building Graph
    adjList = [[] for _ in range(node_count)]
    for i in range(len(edge_start)):
        adjList[edge_start[i]].append(edge_end[i])
        adjList[edge_end[i]].append(edge_start[i])

    visited = [-1 for _ in range(node_count)]
    parent = [-1 for _ in range(node_count)]
    num_components = 0

    # BFS
    def bfs_helper_has_cycle(node):
        q = collections.deque()
        visited[node] = 1
        q.append(node)
        while q:
            v = q.popleft()
            for neighbour in adjList[v]:
                if visited[neighbour] == -1:  # Tree edge
                    visited[neighbour] = 1
                    parent[neighbour] = node
                    q.append(neighbour)
                else:
                    if neighbour != parent[v]:
                        return True
        return False

    # Traverse through each vertex.
    for v in range(node_count):
        # Check visited
        if visited[v] == -1:
            num_components += 1
            if num_components > 1:
                return False
            if bfs_helper_has_cycle(v) == True:
                return False
    return True

n = 4
from_edge = [0, 0, 0]
to_edge = [1, 2, 3]
print(is_it_a_tree_Sunee(n, from_edge, to_edge))