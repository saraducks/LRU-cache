from src import node

class LRU:

    #initailize the node and cache
    def __init__(self):
        self.head_node = node.Node()
        self.cachedata = node.Cache()

    '''
      get the node and add to linked list and calls the addcache to update the hash table
    '''
    def addnode(self, key, value):
        #create node
        added_node = node.Node(key, value)
        #check if node is created
        print("adding node")
        print(added_node)
        # add the node to linked list
        #check if the node head and tail is None
        if(self.head_node.Head == None):
            self.head_node.Head = added_node
            self.cachedata.first = added_node               #udpate the cahcedata head and tail
            self.cachedata.last = added_node
        #if the head is not none, then add the new node
        else:
            self.head_node.previous = added_node
            added_node.next = self.head_node
            self.head_node.Head = added_node
            self.cachedata.first = added_node

    '''
      Remove the least used node
    '''
    #def removenode(self, node, key):







# create node and call addnode
n = LRU()
n.addnode('a',1)
n.addnode('b',2)
n.addnode('c',3)
n.addnode('d',4)
