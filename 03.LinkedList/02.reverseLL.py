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

    # Iterative approach to reverse linked list
    def reverseIterative(self):
        prev = None
        curr = self.head
        while curr is not None:
            # Store the next node
            next_node = curr.next
            
            # Reverse the current node's pointer
            curr.next = prev
            
            # Move pointers one position ahead
            prev = curr
            curr = next_node
            
        # Set the new head
        self.head = prev


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
    llist.reverseIterative()
    print("\nLinked List after Iterative Reverse:")
    llist.printList()
    