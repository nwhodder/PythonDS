class DataStructures:

    #Initiate Class Array(List) from inputted integers
    def __init__(self, *args):
        self.list = [*args]

    #Test method to get sum of all integers in list
    def addall(self):
        return sum(self.list)