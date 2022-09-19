class LinkedList(object):
    # Description: This class implements the Linked List data structure
    #              IMPORTANT: Our operations are always from the perspective of the current node. 
    #                         To work with the entire Linked List, use the "getHead" method.

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
    # >>>>>>>>>>>>>>>>>>>>>
    # Helper Functions
    def getHead(self):
        # Description: Since we are working with only a node class, this method finds the head of the entire LinkedList
        if self.prev is None:
            return self 
        else:
            return self.prev.getHead()
    
    def getListForward(self):
        # Description: This method creates a list of all the data from the current node onwards
        if self.next is None:
            return [self.data]
        else:
            return [self.data] + self.next.getListForward()

    def getAll(self):
        # Description: This method creates of a list of all of the data in the entire LinkedList
        head = self.getHead()
        return head.getListForward()
    # <<<<<<<<<<<<<<<<<<
    
    def prepend(self, item):
        # Description: insert an item at the start of the LinkedList starting at the current node
        # Parameters: Item, an object type 'LinkedList'

        self.insert(0, item)

    def append(self, item):
        # Description: insert an item at the end of the LinkedList starting at the current node
        # Parameters: Item, an object type 'LinkedList'

        self.insert(self.length(), item)

    def insert(self, index, item):
        # Description: insert an item at a specified location, indexed at 0 away from current
        # Parameters: Index, a valid index type 'int'
        #             Item, an object type 'LinkedList'
        # Notes: I chose to specify the location in terms of index, instead of LinkedListNode, so that each item has an obvious unique key 
        # This means that multiple nodes with the same data can exist and that we do not need to resort to other tracking methods 
        # like hashes. 

        if index==0: # Insert an Item at Current Node
            # Previous Node to New Node Connections
            if not self.prev is None:
                self.prev.next = item 
                item.prev = self.prev 
            # New Node to Current Node Connections 
            self.prev = item 
            item.next = self 
        elif index==1 and self.next is None: # Edge Case, Where we append to the end of the list
            self.next = item 
            item.prev = self
        else:
            assert(not self.next is None)
            self.next.insert(index-1, item)

    def delete(self, data):
        # Description: delete an item from the LinkedList starting at the current node given the data
        # Parameters: Data, the value to remove from the LinkedList
        # Return: LinkedList node after deletion, rightmost node after deletion
        # Notes: Since multiple nodes with the same data may exist, we delete the first occurence we encounter

        if self.data == data:
            if self.prev is None and self.next is None: # Current Node is the only node in the LinkedList
                self = None
                return None 
            elif self.prev is None: # Current Node is start of the LinkedList
                self.next.prev = None 
                return self.next 
            elif self.next is None: # Current Node is end of the LinkedList
                self.prev.next = None 
                return self.prev 
            else: # Current Node is in the middle of the LinkedList
                self.prev.next = self.next 
                self.next.prev = self.prev 
                return self.prev 
        else:
            assert(not self.next is None)
            return self.next.delete(data)

    def length(self):
        # Description: Determines the number of elements in the LinkedList starting at the current node

        return len(self.getListForward())
    
    def search(self, target):
        # Description: Return the LinkedList node with the target data
        # Parameters: target, the value we are looking for
        # Return: LinkedList node with target data

        if self.data == target:
            return self

        if not self.next:
            return None

        return self.next.search(target)   

    
