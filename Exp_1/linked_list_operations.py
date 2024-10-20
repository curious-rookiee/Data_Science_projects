# linked_list_operations.py

from node import Node  # Importing the Node class

# Function to find the middle of the linked list
def getMiddle(head):
    if not head:  
        return None
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data

def pushNode(head_ref, data_val):
    new_node = Node(data_val)
    new_node.next = head_ref 
    return new_node

def printList(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")
