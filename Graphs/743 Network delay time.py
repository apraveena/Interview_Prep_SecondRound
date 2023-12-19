class Solution:
    from typing import List
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq

        adj_list = [[] for _ in range(n + 1)]

        for u, v, w in times:
            adj_list[u].append((v, w))

        visited = [-1] * (n + 1)
        visited[0] = 1
        pq = [(0, k)]

        t = 0
        while pq:
            cost, node = heapq.heappop(pq)
            if visited[node] == -1:
                visited[node] = 1
                t = max(t, cost)
                for nei, nei_cost in adj_list[node]:
                    if visited[nei] == -1:
                        heapq.heappush(pq, (nei_cost + cost, nei))

        return -1 if -1 in visited else t

sln = Solution()
print(sln.networkDelayTime(times = [[1,2,1]], n = 2, k = 2))
# print(sln.networkDelayTime(times = [[2,1,4],[2,3,1],[3,4,1], [1, 6, 8], [1, 5, 2]], n = 6, k = 2))
# print(sln.networkDelayTime(times = [[2,1,4],[2,3,1],[3,4,1]], n = 4, k = 2))



































