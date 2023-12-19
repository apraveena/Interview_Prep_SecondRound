#Code for geeksForGeeks
# https://www.geeksforgeeks.org/sort-linked-list-0s-1s-2s-changing-links/
# Python3 Program to sort a linked list
# 0s, 1s or 2s by changing links
import math
# Link list node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Node* newNode( data)
# Sort a linked list of 0s, 1s and 2s
# by changing pointers.
def sortList(head):
    if (head == None or
            head.next == None):
        return head

    # Create three dummy nodes to point to
    # beginning of three linked lists.
    # These dummy nodes are created to
    # avoid many None checks.
    zeroD = Node(0)
    oneD = Node(0)
    twoD = Node(0)

    # Initialize current pointers for three
    # lists and whole list.
    zero = zeroD
    one = oneD
    two = twoD

    # Traverse list
    curr = head
    while (curr):
        if (curr.data == 0):
            zero.next = curr
            zero = zero.next
            curr = curr.next
        elif (curr.data == 1):
            one.next = curr
            one = one.next
            curr = curr.next
        else:
            two.next = curr
            two = two.next
            curr = curr.next

    # Attach three lists
    zero.next = (oneD.next) if (oneD.next) \
        else (twoD.next)
    one.next = twoD.next
    two.next = None

    # Updated head
    head = zeroD.next

    # Delete dummy nodes
    return head


# function to create and return a node
def newNode(data):
    # allocating space
    newNode = Node(data)

    # inserting the required data
    newNode.data = data
    newNode.next = None
    return newNode


# Function to print linked list
def printList(node):
    while (node != None):
        print(node.data, end=" ")
        node = node.next


# Driver Code
if __name__ == '__main__':
    # Creating the list 1.2.4.5
    head = newNode(1)
    head.next = newNode(2)
    head.next.next = newNode(0)
    head.next.next.next = newNode(1)

    print("Linked List Before Sorting")
    printList(head)

    head = sortList(head)

    print("\nLinked List After Sorting")
    printList(head)

# This code is contributed by Srathore
