#Articulation points are nodes that disconnect the component if taken out
#Similar to 1192 critical connections (or bridges) problem
def get_articulation_points(n, connections):
    global time_stamp
    adj_list = [[] for _ in range(n)]
    visited = [-1] * n
    arrival = [-1] * n
    lowest_arrival = [-1] * n
    parent = [-1] * n
    time_stamp = 0
    results = []

    for from_, to_ in connections:
        adj_list[from_].append(to_)
        adj_list[to_].append((from_))

    def dfs(node):
        global time_stamp
        visited[node] = 1
        arrival[node] = time_stamp
        lowest_arrival[node] = time_stamp
        time_stamp += 1
        articulation_flag = False
        for nei in adj_list[node]:
            if visited[nei] == -1:
                visited[nei] = 1
                parent[nei] = node
                child_arrival = dfs(nei)
                lowest_arrival[node] = min(child_arrival, lowest_arrival[node])
                #if lowest arrival time of all my children is greater than or equals me, then I must be critical
                # disconnecting me would break their connection to my ancestors
                if child_arrival >= arrival[node]:
                    articulation_flag = True
            elif nei != parent[node]:
                lowest_arrival[node] = min(lowest_arrival[node], arrival[nei])

        if articulation_flag and node != 0:
            results.append(node)

        return lowest_arrival[node]

    dfs(0)
    nodes_with_0_parent = [node for node in parent if node == 0]
    if len(nodes_with_0_parent) > 1:
        for i in range(1, len(nodes_with_0_parent)):
            results.append(nodes_with_0_parent[i])
    return results

# print(get_articulation_points(4, [[0, 1],[1, 2], [2, 3], [3, 1]]) == [1])
print(get_articulation_points(5, [[0, 1],[1, 2], [2, 3], [3, 1], [3, 4]]) in ([1, 3], [3, 1]))

