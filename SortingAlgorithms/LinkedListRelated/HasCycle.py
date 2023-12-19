class LinkedList:
    def __int__(self):
        self.head = None

    class Node:
        def __init__(self, d):
            next = None
            val = d

    # Utility functions
    # Inserts a new Node at front of the list.
    def push(self, new_data):
        # 1 & 2: Allocate the Node &
        # Put in the data
        new_node = self.Node(new_data)

        # 3. Make next of new Node as head
        new_node.next = self.head

        # 4. Move the head to point to new Node
        self.head = new_node

    # Function to print linked list
    def printList(self):
        temp = self.head
        while temp != None:
            print(str(temp.data), end=" ")
            temp = temp.next
        print()

# Driver program to test above functions
llist = LinkedList()
llist.push(0)
llist.push(1)
llist.push(0)
llist.push(2)
llist.push(1)
llist.push(1)
llist.push(2)
llist.push(1)
llist.push(2)

# Problem : Detect if linked list has a cycle
# Brute force soln 1 :
#   color the node with visited attribute
#   so if a node is being revisited then, there is a cycle
#   Drawback is that we are extending the model and all the consumers need to get the new code
#   Also, if concurrent threads are working at the same time, there can be a mixup
# Soln 2: keep track of visited nodes in a hashmap and check it.
#   We are using O(n) space. If not allowed to use auxiliary space, then next soln is better.
# Sln 3: 2 pointer method where one pointer moves by 1 and second pointer moves by 2.
#   They are bound to meet at some point. Code below.
def has_cycle(head: Node):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
