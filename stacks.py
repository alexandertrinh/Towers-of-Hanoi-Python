import disk

# node class takes in a data object, in this program it's a disk
class node:

    def __init__(self, data):
        self.data = data
        self.next = None


# stack class takes in nodes and connects them through a linked list/;
class stack:

    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, data):
        self.size = self.size + 1
        newNone = node(data)        #disk takes in "size"

