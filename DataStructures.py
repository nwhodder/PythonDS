# Base DS class that others will inherit from
class DataStructures:

    # Initiate Class Array(List) from inputted integers
    def __init__(self, *args):
        self.list = [*args]

    # Test method to get sum of all integers in list
    def addall(self):
        return sum(self.list)
    
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

    # Remove element from Stack
    def remove(self):
        return self.list.pop()
    
