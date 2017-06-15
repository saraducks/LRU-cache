class Node:
    Head = None
    Tail = None
    #doubly linked list with previous and next pointer
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None

'''
  define the capacity of the cache
  add nodes whenever there's a update in the doubly linked list
'''
class Cache(Node):

    def __init__(self, capacity=1024):
        super().__init__()
        self.capacity = capacity
        self.hash = {}
        self.first = Node.Head
        self.last = Node.Tail

