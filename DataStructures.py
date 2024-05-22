# Base DS class that others will inherit from
class DataStructures:

    # Initiate Class Array(List) from inputted integers
    def __init__(self, *args):
        self.list = [*args]

    # Test method to get sum of all integers in list
    def addall(self):
        try:
            return sum(self.list)
        except:
            return "All elements must be an integer to get the sum"
    
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