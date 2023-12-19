# Libraries Included:
# Numpy, Scipy, Scikit, Pandas

# Q. Write some code to create a Deep Clone of a graph

#
# inputs: [1] - 2
#          |    |
#          3  - 4
#
# output: 1 - 2
#         |   |
#         3 - 4


# Definition for a Node.
class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

#my try
class Solution_bfs(object):
    def clone_graph(self, node: Node):
        q = deque()
        q.append(node)
        m = {}
        new_node = Node(node.val)
        m[node] = new_node
        while q:
            curr_node = q.popleft()
            for nei in curr_node.neighbors:
                if nei.val not in m:
                    new_nei = Node(nei.val)
                    # new_node.neighbors.append(new_nei)
                    q.append(nei)
                    m[nei] = new_nei

                m[curr_node].neighbors.append(m[nei])


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution1:
    def clone_graph(self, node: Node) -> Node:
        if not node:
            return node
        old_to_new = {}

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]

            new_node = Node(node.val)
            old_to_new[node] = new_node
            for nei in node.neighbors:
                new_node.neighbors.append(dfs(nei))

            return new_node

        return dfs(node)

from collections import deque

# inputs: [1] - 2
#          |    |
#          3  - 4


node_3 = Node(3)
node_2 = Node(2)
node_4 = Node(4)
node_1 = Node(1)

node_1.neighbors = [node_2, node_3]
node_2.neighbors = [node_1, node_4]
node_3.neighbors = [node_1, node_4]
node_4.neighbors = [node_2, node_3]

sln = Solution1()
result_node = sln.clone_graph(node_1)

# Test the solution
q = deque()
q.append(result_node)
visited = set()
visited.add(result_node.val)

while q:
    curr = q.popleft()
    print("Node: " + str(curr.val))
    for nei in curr.neighbors:
        if nei.val not in visited:
            visited.add(nei.val)
            q.append(nei)
        print("Neighbors: " + str(nei.val))
















