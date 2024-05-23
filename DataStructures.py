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


# Class for Linked List
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

    # Delete first node of LL
    def delFirst(self):
        if self.head is None: # Cancel if there are no nodes
            return
        self.head = self.head.next  # Set new head as next node

    # Delete last node of LL
    def delLast(self):
        if self.head is None:
            return
        node = self.head
        while node.next.next:   # while the current node's pointer has a pointer, move up one position
            node = node.next
        node.next = None        # Move to last node with a pointer and remove that pointer
    
    # Delete node at given index of LL
    def delIndex(self, index):
        node = self.head
        position = 0
        if index == position:   # If index = 0 delete head
            self.delFirst()
        else:
            while node != None and (position + 1) != index: # Parse through our nodes until at position before index
                position += 1
                node = node.next
            if node != None:            # When at correct position before index, change pointer to be the node
                node.next = node.next.next      # after the next 
            else:
                print("Index is out of bounds")

    # Update node at given index of LL
    def updateNode(self, data, index):
        current_node = self.head
        position = 0
        if index == position:
            current_node.data = data
        else:
            while current_node != None and position != index:
                position += 1
                current_node = current_node.next
            if current_node != None:
                current_node.data = data
            else:
                print("Index is out of bounds")
    
    # Function to search index
    def getIndex(self, index):
        current_node = self.head
        if current_node is None:
            print("No nodes exist.")
        else:
            position = 0
            if index == position:
                print(current_node.data)
            else:
                while current_node != None and position != index:
                    position += 1
                    current_node = current_node.next
                if current_node != None:
                    print(current_node.data)
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


# Class For Doubly Linked List
class DoublyLinkedList(DataStructures):
    def __init__(self, *args):
        self.head = None
        self.tail = None
        for arg in args:
            self.insertEnd(arg)

    # Function to add to the end of DLL
    def insertEnd(self, data):
        new_node = self.DLLNode(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
    # Function to add to the beginning of DLL
    def insertStart(self, data):
        new_node = self.DLLNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    # Function to insert at index
    def insertIndex(self, data, index):
        new_node = self.DLLNode(data)
        current_node = self.head
        position = 0
        if index == position:
            self.insertStart(data)
        else:
            while current_node != None and (position + 1) != index:#    [1,2,3,4,5]
                position += 1
                current_node = current_node.next
            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
                new_node.prev = current_node.data
            else:
                print("Index out of bounds")
            
    # Function to delete head of DLL
    def delHead(self):
        if self.head is None:
            return
        else:
            self.head = self.head.next
            self.head.prev = None

    # Function to delete tail of DLL
    def delTail(self):
        if self.tail is None:
            return
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    # Function to delete given index of DLL
    def delIndex(self, index):
        current_node = self.head
        position = 0
        if index == position:
            self.delHead
        else:
            while current_node != None and (position + 1) != index:
                position += 1
                current_node = current_node.next
            if current_node != None:
                current_node.next = current_node.next.next
                current_node.next.prev = current_node
            else:
                print("Index is out of bounds")


    # String function for DLL
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


    # Node class for DLL which now includes a previous pointer
    class DLLNode:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None