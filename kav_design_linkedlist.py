class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, val):
        node = ListNode(val)
        if self.head is None: # check if there is no any element in the node. if yes make the head that you created as the node
            self.head = node
            return #if you dont return here: its an  infinite loop
        
        already_existed = self.head # or makethe already existed node as th head
        while True:
            if already_existed.next is None: # check to see if it is the only element
                already_existed.next = node
                break
            already_existed = already_existed.next


    def printlinkedlist(self):
        current_node = self.head
        while current_node:
            print(current_node.val, end = '-->',)
            current_node = current_node.next
        print('None')


ll = LinkedList()
ll.printlinkedlist()
ll.insert(2)
ll.printlinkedlist()
ll.insert(4)
ll.printlinkedlist()
ll.insert(6)
ll.printlinkedlist()




