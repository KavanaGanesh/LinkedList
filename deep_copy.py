# Algorithm: (Remember: as we move from node to another we cannot create a node and then connect : this method fails - sometimes the random pointer points to node to node that is not even created)
# 1st pass : take each input node and create a copy of the node - not link them yet, map the old node to the new node using hashmap
    # while current node is present:
        # make a copy of the current node value and insert it to the hashmap
# 2nd pass : connect the nodes with the link. Connect the random link here as well


from typing import Optional

class ListNode:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None): #type:ignore
        self.val = int(x)
        self.next = next
        self.random = random


class LinkedList():
    def __init__(self, head = None):
        self.head = head

    def insert(self, val):
        if self.head is None:
            self.head = node
            return 
        
        already_existed = self.head
        while True:
            if already_existed.next is None:
                already_existed.next = node
                break
            already_existed = already_existed.next

    def printList(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.val, end = '->')
            current_node = current_node.next
        print('None')


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dictmap = {None:None}

        current = head
        while current is not None:
            dictmap[current] = Node(current.val)
            current = current.next

        current = head
        while current is not None:
            ptr = dictmap[current]
            ptr.next = dictmap[current.next]
            ptr.random = dictmap[current.random]
            current = current.next
        
        return dictmap[head]



# to do to pritn and see the result

if '__name__ == __main__':
    head = [[3,'null'],[7,3],[4,0],[5,1]]
    
    ll = LinkedList()
    for i in head:
        node = ListNode(i)
        ll.insert(node)
    ll.printList()
    Solution().copyRandomList(ll.head)
    ll.printList()
