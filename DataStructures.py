# Base DS class that others will inherit from
class DataStructures:

    # Initiate Class Array(List) from inputted integers
    def __init__(self, *args):
        self.list = [*args]

    # String method so when object is called it returns the list
    def __str__(self) -> str:
        return f"{self.list}"


# Class for Stack DS
class Stack(DataStructures):

    def __init__(self, *args):
        super().__init__(*args)

    # Add element to Stack
    def add(self, e):
        self.list.append(e)
        return self.list

    # Remove last added element from Stack
    def remove(self):
        return self.list.pop()
    

# Class for Queue DS
class Queue(DataStructures):

    def __init__(self, *args):
        super().__init__(*args)

    # Add element to Queue
    def add(self, e):
        self.list.append(e)
        return self.list
    
    # Remove first element from Queue
    def remove(self):
        return self.list.pop(0)

class LinkedList(DataStructures):

    def __init__(self, *args):
        self.head = None
        if args:
            for arg in args:
                self.insertEnd(arg)

    # Function to insert at the beginning of the LL
    def insertBeginning(self, data):
        new_node = self.LLNode(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    # Function to insert at the end of the LL
    def insertEnd(self, data):
        new_node = self.LLNode(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
        current_node.next = new_node
    
    # Function to get size of ll
    def getSize(self):
        sum = 0
        if self.head:
            current_node = self.head
            while current_node:
                sum += 1
                current_node = current_node.next
        return sum
    
    # Insert and index (starting from 0)
    def insertIndex(self, data, index):
        node = self.LLNode(data)
        current_node = self.head
        position = 0
        if index == position:   # If index = 0 insert as new head
            self.insertBeginning(data)
        else:
            while current_node != None and (position + 1) != index: # Parse through our nodes until at position before index
                position += 1
                current_node = current_node.next
            if current_node != None:            # When at correct position and a node exists after, 
                node.next = current_node.next   # Sets next of new node to the next of the node at position
                current_node.next = node        # Sets next of the node at position to our new node's data
            else:
                print("Index is out of bounds")


    # Str Method for LL
    def __str__(self) -> str:
        node = self.head
        list = []
        while(node):
            list.append(node.data)
            if node.next is None:
                break
            else:
                node = node.next
        return f"{list}"

    # A Node Class for our Linked List which will hold the data and its pointer
    class LLNode:
        def __init__(self, data):
            self.data = data
            self.next = None
