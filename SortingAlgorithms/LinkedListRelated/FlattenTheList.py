#Problem:
#   Linked list has nodes with value, next and child links.
#   There can be multiple disconnected linked lists.
#   As we are tranversing the nodes, If child is found for one of the nodes,
#   that should get attached to the end of the linked list

#Soln 1: Keep track of child nodes in queue
# Traverse the linked list and add child nodes to the queue as we see them
# Deque the child node as we reach the end of the current linked list and attach that to the end
# Keep traversing for that node if the next value is not none.
# Time complexity is O(n) and space complexity can be linear as well to store the items in queue.

#Soln 2: 2 pointer solution
#   where one pointer is waiting at the node that has child while other traverses to the end of the linked list
#   As the end of the linked list is reached, the node at first pointer will get attached to the end of
#   the linked list and we start traversing from that node again.
#   Time complexity = O(n) + O(n) = O(2n) -- still linear (code below)

class Node:
    def __init__(self, data):
        self.next = None
        self.val = data
        self.child = None

def get_tail(curr: Node) -> Node:
    while curr.next:
        curr = curr.next
    return curr

def flatten_the_list(head: Node):
    node = head
    tail = get_tail(node)
    while node:
        if node.child:
            tail.next = node.child
            tail = get_tail(node.child)
        node = node.next

#------------------------------------------------------