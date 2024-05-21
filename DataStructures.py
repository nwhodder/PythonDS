class DataStructures:
    def __init__(self, *args):
        self.list = [*args]

    def addall(self):
        return sum(self.list)