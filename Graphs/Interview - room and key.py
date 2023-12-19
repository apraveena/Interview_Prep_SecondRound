'''

 There are n rooms labeled from 0 to n - 1
 All rooms are locked except for room 0
 You cannot enter a locked room without a key
 When you visit a room, you may find a set of distinct keys that you take with you
 Each key has a number on it, denoting the root that it unlocks
 Return true if you can visit all rooms and false otherwise


 Example
 Input: rooms = [[1],[2],[3],[]]
 Input: rooms = [[1, 2, 3],[2, 3, 4],[3, 2, 4],[1, 2, 3]]
 Output: true
'''


# Time complexity = O(m+n) given m = no. of nodes and n = no. of edges
# Space complexity = O(m+n)
def are_all_rooms_visited(rooms):
    if not rooms:
        return True

    size = len(rooms)
    visited = [-1] * size

    def dfs(node):
        visited[node] = 1
        for nei in rooms[node]:
            if visited[node] == -1:
                dfs(nei)

    dfs(0)
    for i in len(visited):
        if visited[i] == -1:
            return False

    return True


print(are_all_rooms_visited(rooms=[[1], [2], [3], []] == True))