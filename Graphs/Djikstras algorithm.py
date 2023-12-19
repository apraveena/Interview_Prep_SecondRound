def shortest_path(n, connections, src, dest):
    def mst(n, connections):
        import heapq
        adj_list = [[] for _ in range(n)]
        distance = [-1] * n
        captured = [-1] * n
        pq = [] #Prioritity queue -  we are going to use heapq and use minheap functionality to pop the min weight value

        for u, v, cost in connections:
            adj_list[u].append((v, cost))
            adj_list[v].append(u, cost) #if undirected, keep this line, otherwise remove

        distance[src] = 0
        captured[src] = 1  # assuming first one is already captured

        for nei, cost in adj_list[src]:
            heapq.heappush(pq, (cost, nei))
            # heapq.heappush(pq, (nei, cost))

        while pq:
            # TODO: needs to fix the line below
            priority, node = heapq.heappop(pq) #need correct implementation to pop the min priority item based on cost/priority/weight
            # node, priority = heapq.heappop(pq) #need correct implementation to pop the min priority item based on cost/priority/weight
            if captured[node] == 1:
                continue
            captured[node] = 1
            distance[node] = priority
            for nei, cost in adj_list[node]:
                if captured[nei] == -1:
                    heapq.heappush(pq, (distance[node] + cost), nei)
                    # heapq.heappush(pq, (nei, distance[node] + cost))

        return distance[dest]

conn = [[a, d, 10], [a, c, 5], [a, b, 8], [c, e, 1], [e, d, 1], [d, a ,2]]