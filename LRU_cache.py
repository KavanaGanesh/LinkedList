# Least Recently Used (LRU) : web browser like chrome , safari are designed like this
# things to know before solving:
# 1. cache size is fixed of certain capacity
# 2. get method - If key exists -  then return its value else return -1
# 3. set method -
    # any new key - add the key value pair
        # any new pair causes cache to exceed its capacity - remove least recently used key
    # if key already present - update the value of the key

# Algorithm understanding:O(1) complexity: throw a hashmapp to store key-value pairs
# given ; capacity = 2
# idea : storing the value and poinitng a pointer to the respective node(ex : please refer LRU_cache.png file)
# hashmap: Key : 1              2
#         value : 1             2
# Keep 2 dummy nodes , left = least rescently used; right = most recently used (swap right to left and vice versa for eviction)
# use a DOUBLE-LINKEDLIST


# Implementation:
# Input = ["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]
# Ouptut = [null, null, 10, null, null, 20, -1]
# "LRUCache", [2] - capacity is 2
#  "put", [1, 10] - hashmap = {1:10} ; right = {1:10}
# for every key found:we update the left and right node
# "get" , [1] = output = [10]; update: right = {1:10}
# "put", [2, 20] - hashmap = {1:10 ; 2:20} , left = {1:10} right = {2:20}
# "put", [3, 30] - hashmap = {2:20 ; 3:30} ; left = {2:20}, right = {3:30}
# for every key found:we update the left and right node
# "get", [2] , hashmap = {2:20 ; 3:30} ; output = {20}, left = {3:30}; right = {2:20}
# for every key found:we update the left and right node
# "get", [1] , output = -1


# Design a DLL:
class Listnode():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    # insert to the DLL : between prev_node ->right_node
    def insert(self, node):
        prev_node = self.right.prev
        nxt_node =  self.right
        prev_node.next = nxt_node.prev = node
        node.prev = prev_node
        node.next = nxt_node
        

    # remove node from the DLL: prevnode ->NODE-->nxtnode 
    def remove(self, node):
        prev_node = node.prev
        nxt_node = node.next
        prev_node.next = nxt_node
        nxt_node.prev = prev_node

    
class LRUCache():
    def __init__(self, capacity:int):
        self.capacity = capacity
        self.cache = {} #create a hashmap to store key-value

        # left node - gives least recently used
        # right node - gives most recenlty used
        self.left = Listnode(0,0) #create a dummy left node 
        self.right = Listnode(0,0) #create a dummy right node
        self.left.next = self.right #connect these two nodes initially
        self.right.prev = self.left 

    def get(self, key:int) ->int:
        if key in self.cache:
            # if key is found - update the linkedlist :how? use insert and remove method
            self.insert(self.cache[key])
            self.remove(self.cache[key])
            return self.cache[key].value
        return -1
    

    def put(self, key: int, value: int)-> None:
        if key in self.cache:#if key already present then remove key and create a new nodewith same key-value
            self.remove(self.cache[key])
            self.cache[key] = Listnode(key, value) 
            self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # remove from the list and delete LRU from the hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

if '__name__ == __main__':
    Input = ["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]
    ll = LRUCache(2)
    for i in Input:
        node = Listnode(i)
        
ll.put(1, 10)
ll.get(1)
ll.put(2, 20)
ll.put(3, 30)
ll.get(2)
ll.get(1)