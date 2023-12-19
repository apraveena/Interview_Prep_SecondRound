def can_be_divided(n, dislike1, dislike2):
    """
    Args:
     num_of_people(int32)
     dislike1(list_int32)
     dislike2(list_int32)
    Returns:
     bool
    """
    adj_list = [[] for _ in range(n)]
    visited = [-1] * n
    color = [-1] * n
    colors = ["red", "blue"]

    for i in range(len(dislike1)):
        adj_list[dislike1[i]].append(dislike2[i])
        adj_list[dislike2[i]].append(dislike1[i])

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

print(can_be_divided(5,[0, 1, 1, 2, 3],[2, 2, 4, 3, 4]) == True)