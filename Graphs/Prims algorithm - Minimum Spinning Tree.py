def mst(n, connections):
    # from queue import PriorityQueue
    import heapq
    adj_list = [[] for _ in range(n)]
    total_cost = 0

    for u, v, cost in connections:
        adj_list[u].append((v, cost))
        adj_list[v].append(u, cost)

    captured = [-1] * n
    captured[0] = 1 #assuming first one is already captured
    pq = []
    for nei, cost in adj_list[0]:
        heapq.heappush(pq, (nei, cost))

    while pq:
        node, priority = heapq.heappop(pq)
        if captured[node] == 1:
            continue
        captured[node] = 1
        total_cost += priority
        for nei in adj_list[node]:
            if captured[nei] == -1:
                heapq.heappush(pq, (nei, cost))

    return total_cost



'''Pseudocode'''
#incomplete implementation as decrease key cannot be implemented
def mst_not_implemented(n, connections):
    # from queue import PriorityQueue
    import heapq
    adj_list = [[] for _ in range(n)]
    total_cost = 0

    for u, v, cost in connections:
        adj_list[u].append((v, cost))
        adj_list[v].append(u, cost)

    captured = [-1] * n
    visited = [-1] * n
    importance = [-1] * n
    captured[0] = 1 #assuming first one is already captured
    visited[0] = 1
    # importance[0] = 1 #?
    pq = []
    for nei, cost in adj_list[0]:
        heapq.heappush(pq, (nei, cost))

    while pq:
        node, cost = heapq.heappop(pq)
        total_cost += cost
        for nei, cost in adj_list[node]:
            if visited[nei] == -1:
                visited[nei] = 1
                heapq.heappush(pq, (nei, cost))
                importance[nei] = cost
            else:
                if captured[nei] == -1:
                    if cost < importance[nei]:
                        importance[nei] = cost
                        #From Omkar's video of Prim's algorithm implementation
                        # at the very end, he mentions that decrease key cannot be implemented ..
                        # which is what we need to do here
                        # heapq._siftdown(pq, 0, q.index((nei, cost))) ?
                        # heapq._siftdown(Q, 0, Q.index(Qd[v])) from https://github.com/ActiveState/code/blob/master/recipes/Python/577892_Dijkstrshortest_path/recipe-577892.py
                        #Since decrease key cannot be implemented, we are going to find a workaround


    return total_cost



def priority_queue_test():
    from queue import PriorityQueue
    q = PriorityQueue()

    q.put(4)
    q.put(2)
    q.put(5)
    q.put(1)
    q.put(3)

    while q:
        next_item = q.get()
        print(next_item)

    #another example to print in the reverse order
    numbers = [9, 1, 4, 5]
    q = PriorityQueue()
    for number in numbers:
        q.put((-number, number))

    while q:
        print(q.get()[1])


priority_queue_test()