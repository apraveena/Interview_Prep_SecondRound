# airbnb facebook spread the message
#Airbnb - Cover all vertices with the least number of vertices
#Given a directed graph G(can contain subgraphs and cycles), find the minimum number of vertices from which all nodes are reachable
#Facebook - Minimum number of people to spread a message
# Sham-Poobanana problem

def strong_connection_in_2_passes(edges, n):
    adj_list = [[] for _ in range(n + 1)]
    reverse_adj_list = [[] for _ in range(n + 1)]

    for from_edge, to_edge in edges:
        adj_list[from_edge].append(to_edge)
        # reverse_adj_list[to_edge].append(from_edge) - this can be done instead of the code below?

    for vertex in range(1, n + 1):
        for nei in adj_list[vertex]:
            reverse_adj_list[nei].append(vertex)

    visited = [-1] * (n + 1)
    reversed_visited = [-1] * (n + 1)
    visited[0] = 1  # we are not using 0 index.
    reversed_visited[0] = 1  # we are not using 0 index.

    def dfs(node):
        visited[node] = 1
        for nei in adj_list[node]:
            if visited[nei] == -1:
                dfs(nei)

    def reversed_dfs(node):
        reversed_visited[node] = 1
        for nei in reverse_adj_list[node]:
            if reversed_visited[nei] == -1:
                reversed_dfs(nei)

    results = []
    #Launch dfs
    no_of_components = 0
    for v in range(1, n + 1):
        if visited[v] == -1:
            no_of_components += 1
            if no_of_components > 1:
                results.append((1, v))
                return False
            dfs(v)

    #we can also write the above code another way.. will do the other way for reversed search
    reversed_dfs(1)
    if any(visit == -1 for visit in reversed_visited):
        results.append(1, v)
        return False

    return results if len(results) != 0 else True

#Tarjan's algorithm (uses lowest arrival time)
def strong_connection_in_1_pass(edges, n):
    adj_list = [[] for _ in range(n + 1)]
    global time_stamp

    for from_edge, to_edge in edges:
        adj_list[from_edge].append(to_edge)

    visited = [-1] * (n + 1)
    arrival = [-1] * (n + 1)
    lowest_arr = [-1] * (n + 1)
    visited[0] = 1  # we are not using 0 index.
    arrival[0] = 1  # we are not using 0 index.
    lowest_arr[0] = 1 # we are not using 0 index.
    time_stamp = 0
    root = 1

    def dfs(node):
        global time_stamp
        visited[node] = 1
        arrival[node] = time_stamp
        lowest_arr[node] = time_stamp
        time_stamp += 1
        for nei in adj_list[node]:
            if visited[nei] == -1:
                lowest_arr[node] = min(dfs(nei), lowest_arr[node])
            else: #forward/back/cross edge -
                # if forward edge then the arrival time of the neighbor will be greater than my arrival time
                #   so we dont need to check if it's forward edge or not
                # if back edge or cross edge, then my arrival time of my neighbor is smaller than me as
                # my ancestor or sibling is visited first then it was my turn
                # we dont need to check if the neighbor is parent in directed graph
                # because in directed graphs, edge to parent is also back edge
                lowest_arr[node] = min(arrival[nei], lowest_arr[node])
            if lowest_arr[node] == arrival[node] and node != root:
                # there is no way to go to ancestor nodes
                return False

        return lowest_arr[node]

    #Launch dfs
    dfs(root)
    for i in range(1, n + 1):
        if visited[i] == -1:
            return (1, i) # or return False
    return True
