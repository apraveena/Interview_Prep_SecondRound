# class Node(object):
#     def __init__(self, val=0, neighbors=None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []
#
#     def __eq__(self, other_node):
#         return self.val == other_node.val
#
# def clone_graph_Suneetha(node):
#     def bfs(node):
#         from collections import deque
#         if not node:
#             return node
#         q = deque()
#         q.append(node)
#         new_node = Node(node.val)
#         visited_set = set()
#         visited_set.add(node.val)
#         while q:
#             curr = q.popleft()
#             for nei in curr.neighbors:
#                 if nei.val not in visited_set:
#                     new_nei = Node(nei.val)
#                     visited_set.add(nei.val)
#                     q.append(nei)
#                     curr.neighbors.append(new_nei)
#                     new_nei.neighbors.append(curr)
#         return new_node
#
#     return bfs(node)
#


class GraphNode(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(src: GraphNode) -> GraphNode:
    from collections import deque
    # A Map to keep track of all the
    # nodes which have already been created
    m = {}
    q = deque()

    # Enqueue src node
    q.append(src)

    # Make a clone Node
    node = GraphNode()
    node.val = src.val

    # Put the clone node into the Map
    m[src] = node
    while q:
        # Get the front node from the queue
        # and then visit all its neighbors
        u = q.popleft()
        v = u.neighbors
        for neighbor in v:
            # Check if this node has already been created
            if neighbor not in m:
                # If not then create a new Node and
                # put into the HashMap
                node = GraphNode()
                node.val = neighbor.val
                m[neighbor] = node
                q.append(neighbor)

            # Add these neighbors to the cloned graph node
            m[u].neighbors.append(m[neighbor])
    # Return the address of cloned src Node
    return m[src]

def clone_graph_Test():
    from collections import deque
    node_3 = Node(3)
    node_2 = Node(2)
    node_4 = Node(4)
    node_1 = Node(1)

    node_1.neighbors = [node_2, node_3]
    node_2.neighbors = [node_1, node_4]
    node_3.neighbors = [node_1, node_4]
    node_4.neighbors = [node_2, node_3]

    result_node = clone_graph(node_1)

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
            print("Neighbor: " + str(nei.val))

clone_graph_Test()