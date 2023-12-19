def zombie_cluster(zombies):
    """
    Args:
     zombies(list_str)
    Returns:
     int32
    """
    clusters = 0
    n = len(zombies)
    visited = [-1] * n

    def dfs(node):
        visited[node] = 1
        for j in range(n):
            if visited[j] == -1 and zombies[node][j] == '1':
                dfs(j)

    for i in range(n):
        if visited[i] == -1:
            clusters += 1
            dfs(i)

    return clusters

print(zombie_cluster( ["100101", "011000", "011000", "100101", "000010", "100101"]) == 3)
print(zombie_cluster( ["1100", "1110", "0110", "0001"]) == 2)