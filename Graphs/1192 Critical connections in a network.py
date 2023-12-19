#Bridges
#Tarjan's algorithm - includes lowest arrival time list
class Solution:
    from typing import List
    #Bridge/Cut edges: an edge whose removal disconnects the graph
    #Articulation point/Cut vertex: A vertex whose removal disconnects the graph
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # if the node doesn't have a back edge, the edge between it and the parent should be a bridge
        # we will send arrival time of backedges back to parent to propogate above
        # at the end if my arrival time is same as my lowestarrivaltime, edge between me and parent is bridge
        global timestamp
        adj_list = [[] for _ in range(n)]
        result = []
        arrival_time = [-1] * n
        visited = [-1] * n
        parent = [-1] * n
        lowest_arrival_time = [-1] * n
        timestamp = 0
        root = 0
        parent[root] = None

        # 1. Build the graph
        for from_edge, to_edge in connections:
            adj_list[from_edge].append(to_edge)
            adj_list[to_edge].append(from_edge)

        # 2. dfs
        def dfs(node):
            global timestamp
            visited[node] = 1
            timestamp += 1
            arrival_time[node] = timestamp
            lowest_arrival_time[node] = arrival_time[node]

            for nei in adj_list[node]:
                if visited[nei] == -1:
                    parent[nei] = node
                    lowest_arrival_time[node] = min (dfs(nei), lowest_arrival_time[node])
                elif nei != parent[node]:
                    #back edge
                    lowest_arrival_time[node] = min(arrival_time[nei], lowest_arrival_time[node])

                #If I am not root and I cannot be reached from anywhere else
            if parent[node] != None and lowest_arrival_time[node] == arrival_time[node]:
                result.append([parent[node], node])

            return lowest_arrival_time[node]

        #3. outer call
        dfs(root)
        return result
sln = Solution()
print(sln.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]) in ([[1,3]], [[3, 1]]))
