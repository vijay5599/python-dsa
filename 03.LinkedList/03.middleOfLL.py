class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def middleOfLL(self):
        slow = self.head
        fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data
       


# Example usage
if __name__ == "__main__":
    llist = LinkedList()
    
    # Insert elements
    llist.insertAtEnd(1)
    llist.insertAtEnd(2)
    llist.insertAtEnd(3)
    llist.insertAtEnd(4)
    llist.insertAtEnd(5)
    
    print("Original Linked List:")
    llist.printList()
    
    # Using iterative approach
    middle = llist.middleOfLL()
    print("\nmiddle of LL", middle)

    