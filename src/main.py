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
        added_node.next = None
        added_node.previous = None
        #check if node is created
        print("adding node")
        print(added_node)
        # add the node to linked list
        #check if the node head and tail is None
        if(self.head_node.Head == None):
            self.head_node.Head = added_node
            self.head_node.Tail = added_node
            self.cachedata.first = added_node               #udpate the cahcedata head and tail
            self.cachedata.last = added_node
            self.cachedata.hash[key] = added_node           #adding the node and key to hashtable
        #if the head is not none, then add the new node
        else:
            self.head_node.Head.previous = added_node
            added_node.next = self.head_node.Head
            self.head_node.Head = added_node
            self.cachedata.first = added_node
            self.cachedata.hash[key] = added_node             #adding the node and key to hashtable

        return added_node


    '''
      Remove the least used node
    '''
    def removenode(self, remove_node):
        #check if the head is not None
        if(not self.head_node.Head == None):
            # check if the node is head and head equals tail
            if(self.head_node.Head == self.head_node.Tail):
                print("I am executing.....")
                self.head_node.Head = None
                self.cachedata.first = None
                self.cachedata.last = None
                self.cachedata.hash.__delitem__(remove_node.key)

            # check if the node is head and update the cache first
            if(self.head_node.Head == remove_node):
                self.head_node.Head.previous = None
                self.head_node.Head = self.head_node.Head.next
                self.cachedata.first = self.head_node.Head
                self.cachedata.hash.__delitem__(remove_node.key)

            # check if the node is tail and update the cache last
            if(self.head_node.Tail == remove_node):
                self.head_node.Tail = self.head_node.Tail.previous
                self.head_node.Tail.next = None
                self.cachedata.last = self.head_node.Tail
                self.cachedata.hash.__delitem__(remove_node.key)

            #if node is in the middle
            else:
                parent_node = remove_node.previous
                decendant_node = remove_node.next
                parent_node.next = decendant_node
                decendant_node.previous = parent_node
                self.cachedata.hash.__delitem__(remove_node.key)
        return remove_node

    '''
      get method to check if the key is already present move to the head
    '''
    def __get__(self, key):
        # check if the key is already present in hashtable
        if(self.cachedata.hash.__contains__(key)):
            move_to_head = self.cachedata.hash.get(key)      #get the node
            #remove the node from the linkedlist
            removed_node = self.removenode(move_to_head)
            #add the removed node to the head
            added_node_to_head = self.addnode(removed_node.key, removed_node.value)
            return added_node_to_head.key
        else:
            return -1

    '''
      set method to verify if the cache capacity reached it's limit and delete the elements
    '''




# create node and call addnode
# n = LRU()
# n.addnode('a',1)
# n.addnode('b',2)
# n.addnode('c',3)
# n.addnode('d',4)
r = LRU()
r.addnode('x',10)
res = r.addnode('y',20)
r.addnode('z',30)
print(res.key)
r.__get__(res.key)

