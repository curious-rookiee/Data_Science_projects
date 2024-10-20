# main.py

from linked_list_operations import pushNode, printList, getMiddle

# Driver Code
if __name__ == "__main__":
    head = None
    for i in range(1, 9):
        head = pushNode(head, i)
    print("Linked List: ")
    printList(head)
    print("Middle Value Of Linked List is:", getMiddle(head))
