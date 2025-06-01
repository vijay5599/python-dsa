from hmac import new
from operator import ne


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    

    def insertAtBegin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)
        curr = self.head

        while curr.next is not None:
            curr = curr.next
        curr.next = new_node

    def insertAtPosition(self, data, index):
        new_node = Node(data)
        # Handle empty list or insert at beginning
        if self.head is None or index == 1:
            new_node.next = self.head
            self.head = new_node
            return
            
        # Traverse to the position before the insertion point
        pos = 1
        curr = self.head
        
        while curr is not None and pos < index - 1:
            curr = curr.next
            pos += 1
            
        # If we've reached the end or index is out of bounds
        if curr is None:
            print(f"Index {index} is out of bounds")
            return
            
        # Insert the new node
        new_node.next = curr.next
        curr.next = new_node
        


    def printLL(self):
        """Print all elements of the linked list"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def deleteFirst(self):
        """Delete the first node of the linked list"""
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next

    def deleteLast(self):
        """Delete the last node of the linked list"""
        if self.head is None:
            print("List is empty")
            return
        
        # If there's only one node
        if self.head.next is None:
            self.head = None
            return
            
        # Traverse to the second last node
        curr = self.head
        while curr.next.next is not None:
            curr = curr.next
        curr.next = None

    def deleteByValue(self, value):
        """Delete a node with the given value"""
        if self.head is None:
            print("List is empty")
            return
            
        # If the value is in the first node
        if self.head.data == value:
            self.head = self.head.next
            return
            
        # Traverse the list to find the node
        curr = self.head
        while curr.next is not None:
            if curr.next.data == value:
                curr.next = curr.next.next
                return
            curr = curr.next
        
        print(f"Value {value} not found in the list")


llist = LinkedList()
llist.insertAtBegin("a")
llist.insertAtBegin("b")
llist.insertAtBegin("c")
llist.insertAtBegin("e")
llist.printLL()

llist.insertAtEnd("d")
llist.printLL()

print("\nTrying to delete non-existent value 'z':")
llist.deleteByValue("z")
llist.printLL()

# Demonstrate reverse method
print("\nOriginal list:")
llist.printLL()
